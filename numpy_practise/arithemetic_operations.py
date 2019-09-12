# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:46:58 2019

@author: Terralogic
"""
import numpy as np

def fun1():
    a = np.arange(9, dtype=np.float_).reshape(3,3)
    print('First Array : ',a,'\n')
    
    b= np.array([10,10,10])
    print('Second Array : ',b,'\n')
    
    sum_val = np.add(a,b)
    print('Sum Value : ',sum_val,'\n')
    sub_val = np.subtract(a,b)
    print('Subtract value : ',sub_val,'\n')
    mul_val = np.multiply(a,b)
    print('Muliplied Value : ',mul_val,'\n')
    div_val = np.divide(a,b)
    print('Division Value : ',div_val,'\n')
#fun1()    

def fun2():
    a = np.array([0.25, 1.33,1, 0, 100])
    print('First Array Data is : ',a,'\n')
    
    print('After Reciprocal Function Data is : ',np.reciprocal(a),'\n')

    b = np.array([100],dtype=int)
    print('Second array data is : ',b,'\n')
    print('After Reciprocal Function Data is : ',np.reciprocal(b),'\n') 
#fun2()

def fun3():
    a=np.array([10,100,1000])
    print('First Array Data is : ',a,'\n')
    print('After Applied Power Function : ',np.power(a,2),'\n')
    
    b= np.array([3,2,1])
    print('First Array Data is : ',a,'\n')
    print('After Applied Power Function : ',np.power(a,b),'\n')
#fun3()

def fun4():
    a = np.array([10,20,30])
    b = np.array([3,5,7])
    print('First Array Data is : ',a,'\n')
    print('After Applied Mod Function : ',np.mod(a,b),'\n')
    print('After Applied Reaminder Function : ',np.remainder(a,b),'\n')
#fun4()

def fun5():
    a = np.array([-5.6j, 0.2j, 11. , 1+1j])
    print('Original array : ',a,'\n')
    print('After Applied real() Function : ',np.real(a),'\n')
    print('After Applied imag() Function : ',np.imag(a),'\n')
    print('After Applied conj() Function : ',np.conj(a),'\n')
    print('After Applied angle() Function : ',np.angle(a),'\n')
    print('Applying angle() function again (result in degrees)',np.angle(a, deg = True))
fun5()

























