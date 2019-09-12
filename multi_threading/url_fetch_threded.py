import Queue, threading, urllib2, time
hosts = "http://yahoo.com", "http://google.com", "http://ibm.com", "http://apple.com"
queue = Queue.Queue()

class ThreadUrl(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            host = self.queue.get()
            url_local = urllib2.urlopen(host)
            print(url_local.read(1024))
            self.queue.task_done()
start = time.time()
def main():
    for i in range(5):
        t = ThreadUrl(queue)
        t.setDaemon(True)
        t.start()
        for host in hosts:
            queue.put(host)
    queue.join()
main()
print("Elapsed Time: %s" % ((time.time()-start)))
