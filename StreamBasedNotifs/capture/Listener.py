import redis
import threading
import json
from .models import streamListen

class Listener(threading.Thread):
    def __init__(self, r, channels):
        threading.Thread.__init__(self)
        self.redis = r
        self.pubsub = self.redis.pubsub()
        self.pubsub.subscribe(channels)

    def work(self, item):
        streamListen.objects.create(data=item['data'])
        print item['data']


    def run(self):
        for item in self.pubsub.listen():
            if item['data'] == "KILL":
                self.pubsub.unsubscribe()
                print (self, "unsubscribed and finished")
                break
            else:
                self.work(item)
