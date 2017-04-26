import redis
import threading

class Listener(threading.Thread):
    def __init__(self, r, channels):
        threading.Thread.__init__(self)
        self.redis = r
        self.pubsub = self.redis.pubsub()
        self.pubsub.subscribe(channels)

    def work(self, item):
        print (item['channel'], ":", item['data'])

    def run(self):
        for item in self.pubsub.listen():
            if item['data'] == "KILL":
                self.pubsub.unsubscribe()
                print (self, "unsubscribed and finished")
                break
            else:
                self.work(item)

if __name__ == "__main__":
    client = Listener(redis.StrictRedis(host='demo.scorebeyond.com',port=8007), ['test'])
    client.start()

    r.publish('test', 'this will reach the listener')
    r.publish('fail', 'this will not')

    r.publish('test', 'KILL')
