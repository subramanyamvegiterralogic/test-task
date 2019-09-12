# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 16:02:26 2019

@author: Terralogic
"""

import numpy as np
def fun1():
    a = np.array([0,30,45,60,90])
    
    print('Sine of Different angles : ',np.sin(a*np.pi/180),'\n')
    print('Cosine of Different angles : ',np.cos(a*np.pi/180),'\n')
    print('Tangent of Different angles : ',np.tan(a*np.pi/180),'\n')
#fun1()

def fun2():
    a = np.array([0,30,45,60,90])
    sine = np.sin(a*np.pi/180)
    print('Sine Value : ',sine,'\n')
    
    sine_inverse = np.arcsin(sine)
    print('Degrees : ',np.degrees(sine_inverse))
    print('Sine Inverse Value : ',sine_inverse,'\n')
    
    cosin = np.cos(a*np.pi/180)
    print('Cosin Value : ',cosin,'\n')
    
    cosine_inverse = np.arccos(cosin)
    print('Degrees : ',np.degrees(cosine_inverse))
    print('cosine Inverse Value : ',cosine_inverse,'\n')

    tangent = np.tan(a*np.pi/180)
    print('Tangent Value : ',tangent,'\n')
    
    tangent_inverse = np.arctan(tangent)
    print('Degrees : ',np.degrees(tangent_inverse))
    print('Tangent Inverse Value : ',tangent_inverse,'\n')
#fun2()

def fun3():
    a=np.array([1.0,5.55, 123, 0.567, 25.532])
    print('Original Array : ',a,'\n')
    print(np.around(a))
    print(np.around(a, decimals=1))
    print(np.around(a, decimals=-1))
#fun3()

def fun4():
    a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
    print('Original Array : ',a,'\n')
    print('Floor valued Array : ',np.floor(a),'\n')
#fun4()

def fun5():
    a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
    print('Original Array : ',a,'\n')
    print('Ceil valued Array : ',np.ceil(a),'\n')
fun5()





















