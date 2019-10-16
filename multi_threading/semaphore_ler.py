from threading import Semaphore,BoundedSemaphore, Thread, current_thread
import time
import queue
# s = Semaphore()
s = BoundedSemaphore()


def book():
    global tickets
    tickets = 6
    s.acquire()
    if tickets == 0:
        print('Ticket Booked By : ',end ='')
        time.sleep(1)
        print(current_thread().getName())
        print('Reamining Tickets : Sold Out')
        print('If your amount is deducted will credit back in 7-10 working days')
        # return
    else:
        print('Ticket Booked By : ',end ='')
        time.sleep(1)
        print(current_thread().getName())
        tickets -= 1
        print('Reamining Tickets : ', tickets)
        print('Transaction Succesfull, Please check your mail for the confirmation')
        # time.sleep(1)
    print('_________________________________________________________________________________________')
    s.release()


def queue_fun():
    print(current_thread().getName())
    global contat_names
    global q
    q = queue.Queue()
    for i in range(1,10):
        name = 'Person : {}'.format(i)
        q.put(name)


def start_queue_fun():
    while not q.empty():
        Thread(target=book, name=q.get()).start()


Thread(target=queue_fun, name='Queue Thread Begin').start()
while True:
    Thread(target=start_queue_fun, name='Queue Thread Processing').start()
    time.sleep(10)

