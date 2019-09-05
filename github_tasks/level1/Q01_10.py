def question_1():
    res_li=[]
    for i in range (2000,3201):
        if i%7==0 and i%5 !=0:
            res_li.append(str(i))

    print ','.join(res_li)

def question_2():
    fact_val = 0
    def fact(x):
        if x == 0:
            return 1
        return (x * fact(x-1))
    print(fact(8))

def question_3():
    upper_limit = input('Please enter Upper Value : ')
    x = {i:i*i for i in range(0,upper_limit+1)}
    print(x)

def question_4():
    ip_data = raw_input('Please Take Input Data : ').split(',')
    li = list(ip_data)
    print(li)
    tu = tuple(li)
    print(tu)

def question_5():
    class Test:
        def __init__(self):
            self.ip_data = ""

        def getString(self):
            self.ip_data = input('Please Enter input value : ')

        def printString(self):
            print(self.ip_data)
    t = Test()
    t.getString()
    t.printString()

import math
def question_6():
    c,h = 50,30
    ip_data = raw_input('Please Take Input Data : ').split(',')
    li_ip_data = list(ip_data)
    li_output_data=[]
    for item in li_ip_data:
        res = math.sqrt((2*c*int(item))/h)
        li_output_data.append(int(math.floor(res)))
    print(li_output_data)

def question_7():
    final_list = []
    i,j =raw_input('Please Take Input Data : ').split(',')
    for x in range(0,int(i)):
        row_list=[]
        for y in range(0,int(j)):
            row_list.append(x*y)
        final_list.append(row_list)
    for item in final_list:
        print(item)

# question_1()
# question_2()
# question_3()
# question_4()
# question_5()
# question_6()
question_7()