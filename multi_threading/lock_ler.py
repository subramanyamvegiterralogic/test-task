from threading import *
import time
lock = Lock()
def fun():
    with lock:
        for i in range(1,2):
            print('Hello...!  ', end='')
            time.sleep(3)
            print(current_thread().getName())
Thread(target=fun, name='INC').start()
Thread(target=fun, name='TDP').start()
Thread(target=fun, name='CPI').start()
Thread(target=fun, name='CPM').start()
Thread(target=fun, name='BJP').start()
Thread(target=fun, name='MIM').start()
Thread(target=fun, name='TRS').start()
Thread(target=fun, name='TJS').start()
Thread(target=fun, name='JSP').start()
Thread(target=fun, name='YSRCP').start()