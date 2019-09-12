import threading, time

exit_flag = 0

class MyThread (threading.Thread):
    def __init__(self , thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print('Starting : '+self.name)
        print_time(self.name,self.counter, 5)
        print('Exiting : '+self.name)

def print_time(thread_name, counter, delay):
    while counter:
        if exit_flag:
            thread_name.exit()
        time.sleep(delay)
        print('%s : %s'%(thread_name, time.ctime(time.time())))
        counter -= 1

thread1 = MyThread(1,'Terralogic',1)
thread2 = MyThread(2,'Datazymes',2)

thread1.start()
thread2.start()

print('Exiting Main Thread')