# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:44:49 2020

@author: anwar
"""

# Fibonacci with a Dictionary

def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2,d)
        d[n] = ans
        return ans
    
d = {1:1, 2:2}
print(fib_efficient(6, d))

