# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
def fun1():
    a = np.arange(0,60,5)
    a = a.reshape(3,4)
    print(a)
    print('\n')
    
    b=a.T
    print(b)
    print('\n')
    
    c = b.copy(order='C')
    print(c)
    print('\n')
    
    print('\nSorted in C-style order:')
    print(c)
    for x in np.nditer(c):
        print(x)
    
    print('\nSorted in F-style order:')
    c = b.copy(order='F')
    print(c)
    for x in np.nditer(c):
        print(x)
#fun1()
def fun2():
    a = np.arange(0,60,5)
    a=a.reshape(3,4)
    print('Original Array is : ',a,'\n')
    
    for x in np.nditer(a,op_flags = ['readwrite']):
        x[...] = 2*x
    print('Modified Array is : ',a)
#fun2()    

def fun3():
    a = np.arange(0,60,5)
    a = a.reshape(3,4)
    print('Original Array is : ',a,'\n')
    
    print('Modified Array is : ')
    for x in np.nditer(a, flags=['external_loop'], order='F'):
        print(x,end=' ')
#fun3()

def fun4():
    a = np.arange(0,60,5)
    a = a.reshape(3,4)
    print('First Array is : ',a,'\n')
    
    b = np.array([1,2,3,4],dtype=int)
    print('Second Array is : ',b,'\n')
    
    print('Modified Array is : ')
    for x,y in np.nditer([a,b]):
        print('%d : %d'%(x,y))
fun4()