import json
import logging
from channels import Channel
from channels.sessions import channel_session
from .models import Stream
import redis
import ast
from .views import captureEvents
from django.shortcuts import redirect

log = logging.getLogger(__name__)
redis_con = redis.Redis('demo.scorebeyond.com',8007)
subs = redis_con.pubsub()
subs.subscribe('test')

@channel_session
def ws_connect(message):
    message.reply_channel.send({
        "text": json.dumps({
            "action": "reply_channel",
            "reply_channel": message.reply_channel.name,
        })
    })

def ws_capture(message):
    '''Capture redis stream and save it into database'''
    for message in subs.listen():
        if message['type'] == "message":
            data1 = ast.literal_eval(message['data'])
            if not Stream.objects.filter(name=data1['name']):
                typeList = []
                if not data1['info']:
                    Stream.objects.create(name=data1['name'], info="")
                else:
                    for k , v in data1['info'].iteritems():
                        typeList.append(k+":"+type(v).__name__)
                    Stream.objects.create(name=data1['name'], info=','.join(typeList))
                Channel('capture-stream').send({"name":data1['name'],
                                        "info":','.join(typeList),
                                        })
        else:
            print message
