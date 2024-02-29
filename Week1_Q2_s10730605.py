# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 08:37:15 2024

@author: Student
"""
P1=True
Q1=True
P2=False 
Q2=False 
print('==============================')
table1=[
       ['P','Q','P∧Q','P∨Q','P→Q','P←Q','P↔Q'],
       [P1,Q1,P1 and Q1,P1 or Q1,True,True,True],
       [P1,Q2,P1 and Q2,P1 or Q2,False,True,False],
       [P2,Q1,P2 and Q1,P2 or Q1,True,False,False],
       [P2,Q2,P2 and Q2,P2 or Q2,True,True,True]
       ]
for row in table1 :
    print(row)
print('==============================')


