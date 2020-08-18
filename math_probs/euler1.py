#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 23:20:41 2020

@author: nsbhatta

Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def prblm_1_brute():
    
    tot =set()
    for i in range(0,1000,3):
        tot.add(i)
    
    for j in range(0,1000,5): 
        tot.add(j)
    
    
    print(sum(tot))
    
    
if __name__ == "__main__":
    prblm_1_brute()
    