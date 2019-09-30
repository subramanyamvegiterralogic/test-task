import threading, time
from threading import *
def print_thread4():
    for x in range(10,30,2):
        print('Thread 4 Printed \t:\t',x)
        time.sleep(2)
def print_thread2():
    for y in range(10,30,3):
        print(current_thread().getName(),'\t:\t',y)
        time.sleep(3)
def print_thread5():
    for y in range(10,30,4):
        print('Thread 5 Printed \t:\t',y)
        time.sleep(2)

t2 = threading.Thread(target=print_thread2, name='Thread 2').start()
t3 = threading.Thread(target=print_thread2, name='Thread 3').start()
t1 = threading.Thread(target=print_thread2, name='Thread 1').start()
t4 = threading.Thread(target=print_thread4, name='Thread 4').start()
t5 = threading.Thread(target=print_thread5, name='Thread 5').start()