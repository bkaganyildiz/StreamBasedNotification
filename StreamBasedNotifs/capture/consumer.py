from channels import Channel
from channels.auth import channel_session_user_from_http
from .models import Stream, Notification
import redis
import ast
from .task import sendNotifications
from channels import Group
import json
#from djutils.decorators import async

redis_con = redis.Redis('demo.scorebeyond.com', 8007)
subs = redis_con.pubsub()
subs.subscribe('test')

@channel_session_user_from_http
def ws_connect(message):
    '''Capture redis stream and save it into database'''
    Group('stream').add(message.reply_channel)
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
                Group('stream').send({
                    'text': json.dumps({
                        'username': data1['name'],
                        'is_logged_in': True
                    })
                })
        else:
            print message

