# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a=float(input('input a:'))
b=float(input('input b:'))
c=float(input('input c:'))
x=b**2-4*a*c
if x>0:
    print('have 2 different root')
elif x<0:
    print('have no root')
else:
    print('have 1 real root')
    
