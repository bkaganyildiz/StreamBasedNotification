from background_task import background
from .models import Notification
import  requests
import json
from .models import Stream, Notification
import redis
import ast
import logging
logger = logging.getLogger('StreamBasedNotifs')
hdlr = logging.FileHandler('notifications.log')
formatter = logging.Formatter('%(asctime)s  %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)

@background(schedule=0)
def sendNotifications(data):
    '''send delayed notifications to webhook url'''
    notif_features = Notification.objects.get(event_name=data['name'])
    webhook_url = notif_features.url
    slack_data = {}
    slack_data['info'] = data['info']
    target_data = []
    if not notif_features.target : # If target has been set as User
        target_data.append(data['user_id'])
        slack_data['target'] = target_data
    else:
        slack_data['target'] = data['associated_user_ids']
    slack_data['event_name'] = data['name']
    slack_data['name'] = notif_features.name
    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code/100 != 2:
        logger.error(
            '%s \n %s'
            % (str(response.status_code), data)
        )

@background(schedule=-1)
def listen_stream():
    redis_con = redis.Redis('demo.scorebeyond.com', 8007)
    subs = redis_con.pubsub()
    subs.subscribe('test')
    for message in subs.listen():
        if message['type'] == "message":
            data1 = ast.literal_eval(message['data'])
            print data1['name']
            if Notification.objects.filter(event_name=data1['name']):
                print "hello"
                sendNotifications(data1, capture=Notification.objects.get(event_name=data1['name']).delay)
            if not Stream.objects.filter(name=data1['name']):
                type_list = []
                if not data1['info']:
                    Stream.objects.create(name=data1['name'], info="")
                else:
                    for k, v in data1['info'].iteritems():
                        type_list.append(k+":"+type(v).__name__)
                    Stream.objects.create(name=data1['name'], info=','.join(type_list))
        else:
            print message