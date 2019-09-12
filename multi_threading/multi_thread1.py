import thread, time

def print_time(thread_name, time_deplay):
    count = 0
    while count < 5:
        time.sleep(time_deplay)
        count += 1
        print('%s : %s'%(thread_name, time.ctime(time.time())))

try:
    thread.start_new_thread(print_time,('Terralogic',2,))
    thread.start_new_thread(print_time,('Datazymes',4,))
except:
    print("Error Occured")

while 1:
    pass
