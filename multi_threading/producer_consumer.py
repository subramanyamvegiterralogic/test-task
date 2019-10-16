from threading import *
import time

def prod():
    time.sleep(5)
    print('Prod thread producing items')
    print('Prod thread giving notification')
    event.set()


def consume():
    print('consumer thread waiting for updation')
    event.wait()
    print('Consumer got notification ')

event= Event()
t1 = Thread(target=prod)
t2 = Thread(target=consume)
t1.start()
t2.start()