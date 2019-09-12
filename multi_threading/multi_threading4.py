import threading, time, queue
exit_flag= 0

class MyThread(threading.Thread):
    def __init__(self , thread_id, name, q):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.q = q

    def run(self):
        print('Starting : '+self.name)
        process_data(self.name, self.q)
        print('Exiting : '+self.name)

def process_data(thread_name, q):
    while not exit_flag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (thread_name, data))
        else:
            queueLock.release()
            time.sleep(1)

thread_list = ['thread-1', 'thread-2', 'thread-3']
name_list = ['One', 'Two', 'Three', 'Four', 'Five']
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
thread_id = 1

for thread_name in thread_list:
    thread = MyThread(thread_id, thread_name, workQueue)
    thread.start()
    threads.append(thread)
    thread_id += 1
queueLock.acquire()
for word in name_list:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

exit_flag = 1

for thread in threads:
    thread.join()
print('Exiting the Main Thread')
