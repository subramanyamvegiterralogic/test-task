import collections

class CollectionLer():
    def __init__(self):
        self.de = collections.deque([x for x in range(0,100,9)])

    def add(self, ele):
        self.de.append(ele)

    def add_left(self, ele):
        self.de.appendleft(ele)

    def delete(self):
        self.de.pop()

    def delete_left(self):
        self.de.popleft()

    def search_item_position(self, ele):
        print(self.de.index(ele))

    def insert_in_position(self,position, ele):
        self.de.insert(position, ele)

    def get_count_of_element(self, ele):
        print(self.de.count(ele))

    def remove(self, ele):
        self.de.remove(ele)

    def add_list(self, li_items):
        self.de.extend(list(li_items))

    def add_list_left(self, li_items):
        self.de.extendleft(list(li_items))

    def rotate(self,ele):
        self.de.rotate(ele)
        print(self.de)

    def reverse(self):
        self.de.reverse()
        print(self.de)

c = CollectionLer()
while True:
    print('01) ADD')
    print('02) ADD LEFT')
    print('03) POP')
    print('04) POP LEFT')
    print('05) INDEX')
    print('06) INSERT')
    print('07) REMOVE')
    print('08) EXTEND')
    print('09) EXTEND LEFT')
    print('10) ROTATE')
    print('11) REVERSE')
    print('\n-----------------------------------------------\n')
    choose = input('Choose Functionality From the List \t:\t')
    if choose.upper()=='ADD':
        ele = eval(input('Enter Element \t:\t'))
        c.add(ele)
    elif choose.upper()=='ADD LEFT':
        ele = eval(input('Enter Element \t:\t'))
        c.add_left(ele)
    elif choose.upper()=='POP':
        c.delete()
    elif choose.upper()=='POP LEFT':
        c.delete_left()
    elif choose.upper()=='INDEX':
        ele = eval(input('Enter Element \t:\t'))
        c.search_item_position(ele)
    elif choose.upper()=='INSERT':
        ele = eval(input('Enter Element \t:\t'))
        position = eval(input('Enter Item Position \t:\t'))
        c.insert_in_position(position,ele)
    elif choose.upper()=='REMOVE':
        ele = eval(input('Enter Element \t:\t'))
        c.remove(ele)
    elif choose.upper()=='EXTEND':
        ele = collections.deque(input('Enter Elements \t:\t'))
        c.add_list(ele)
    elif choose.upper()=='EXTEND LEFT':
        ele = collections.deque(input('Enter Elements \t:\t'))
        c.add_list_left(ele)
    elif choose.upper()=='ROTATE':
        ele = eval(input('Enter Element \t:\t'))
        c.rotate(ele)
    elif choose.upper()=='REVERSE':
        c.reverse()
    else:
        print('Your operations was done')
        break
