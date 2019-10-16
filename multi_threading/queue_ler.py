import queue

def add_list_to_queue():
    global list_items
    list_items = ['INC','TDP','CPI','CPM','BJP','MIM','TRS','TJS','JSP','YSRCP']


def priority_queue():
    q = queue.PriorityQueue()
    for item in list_items:
        q.put(item)
    while not q.empty():
        print(q.get(), end=' ')


def lifo_queue():
    q = queue.LifoQueue()
    for item in list_items:
        q.put(item)
    while not q.empty():
        print(q.get(), end=' ')
def gen_queue():
    q = queue.Queue()
    for item in list_items:
        q.put(item)
    while not q.empty():
        print(q.get(), end=' ')

add_list_to_queue()
print('\nPRIORITY QUEUE \t:\t', end=' ')
priority_queue()
print('\nLIFO QUEUE \t:\t', end=' ')
lifo_queue()
print('\nFILO QUEUE \t:\t', end=' ')
gen_queue()
