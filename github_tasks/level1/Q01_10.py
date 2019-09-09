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

def ancient_chinese_puzzle():
    def solve(no_of_heads, no_of_legs):
        ns = 'No Solution'
        for i in range(1,no_of_heads+1):
            j = no_of_heads-i
            if 2*i+4*j == no_of_legs:
                return i,j
        return ns,ns
    chickens , rabbits = solve(35 , 94)
    print('Chickens : ',chickens, 'Rabbits : ',rabbits)
# ancient_chinese_puzzle()

def question_8():
    str_li = raw_input('Please Take Input Data : ').split(',')
    str_li.sort()
    print(','.join(str_li))

def question_9():
    lines = []
    while True:
        s = input()
        if s:
            lines.append(s.upper())
        else:
            break
    for seq in lines:
        print(seq)

def question_10():
    words = list(set(str(input()).split(' ')))
    words.sort(reverse=False)
    print(words)

def question_11():
    value =[]
    items = [x for x in raw_input().split(',')]
    for p in items:
        intp = int(p, 2)
        if not intp % 5:
            value.append(p)
    print ','.join(value)

def question_12():
    li = []
    for i in range(1000,3001,2):
        li.append(str(i))
    print(','.join(li))

def question_13():
    s = str(input())
    dc = {"LETTERS":0 , "DIGITS":0}
    for char in s:
        if char.isalpha():
            dc['LETTERS'] += 1
        elif char.isdigit():
            dc['DIGITS'] += 1
        else:
            pass
    print(dc)

def question_14():
    s = str(input())
    dc = {"UPPER CASE": 0, "LOWER CASE": 0,"TITLE CASE": 0, "DIGITS":0}
    for char in s:
        if char.isupper():
            dc['UPPER CASE'] += 1
        elif char.islower():
            dc['LOWER CASE'] += 1
        elif char.istitle():
            dc['TITLE CASE'] += 1
        elif char.isdigit():
            dc['DIGITS'] += 1
        else:
            pass
    print(dc)

def question_15():
    s = input()
    a =s
    outp = s+(s*s)+(s*s*s)+(s*s*s*s)
    print(outp)
    n1 = int("%s" % a)
    n2 = int("%s%s" % (a, a))
    n3 = int("%s%s%s" % (a, a, a))
    n4 = int("%s%s%s%s" % (a, a, a, a))
    print n1 + n2 + n3 + n4

def question_16():
    s = list(input())
    comp_li = [x for x in s if (x%2!=0)]
    print(comp_li)
#
#  question_1()
# question_2()
# question_3()
# question_4()
# question_5()
# question_6()
# question_7()
# question_8()
# question_9()
# question_10()
# question_11()
# question_12()
# question_13()
# question_14()
# question_15()
question_16()