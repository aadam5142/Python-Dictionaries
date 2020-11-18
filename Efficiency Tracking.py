# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:07:52 2020

@author: anwar 
"""

# Tracking Efficiency

numFibCalls = 0

print(fib(12))
print('function calls', numFibCalls)

numFibCalls = 0

d = {1:1, 2:2}
print(fib_efficient(12, d))
print('function calls', numFibCalls)


