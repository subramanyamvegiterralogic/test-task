import threading, time

class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print('Starting : '+self.name)
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        threadLock.release()

def print_time(thread_name, counter, delay):
    while counter:
        time.sleep(delay)
        print('%s : %s '%(thread_name, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

t1 = MyThread(1,'Act Fibernet',3)
t2 = MyThread(2,'Terralogic',3)
t3 = MyThread(3,'Datazymes',3)

t1.start()
t2.start()
t3.start()

threads.append(t1)
threads.append(t2)
threads.append(t3)

for t in threads:
    t.join()
print('Exiting Main Thread')