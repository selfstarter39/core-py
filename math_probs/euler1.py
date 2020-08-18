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
    return None
    


def btr_soln():
    """
    
    Let's use formula for AP:
    SumDivisibleBy(3) + SumDivisibleBy(5) - SumDivisibleBy(15)
    
    Multiple of 3: 3 6 9 12 ..999
    Sum of these are: 3 + 6 + 9 + 12 + ..+ 999
    = 3(1+2+3+4+..+333) = 3 * 333 * 334/2
    
    Similarly multiple of 5: 5 10 15 20 ..995
    = 5(1 + 2 + 3 + 4 + ..+ 199) = 199 * 200 * 5/2
        
    Similarly multiple of 15: 15 30 45 ..990
    = 15(1 + 2 + ...+ 66) = 15 * 66 * 67 /2

    Returns
    -------
    None.

    """
    s3 = 3 * 333 * 334/2
    s5 = 199 * 200 * 5/2
    s15 = 15 * 66 * 67 /2
    
    print(s3 + s5 - s15)
    
    

    
if __name__ == "__main__":
    #prblm_1_brute()
    btr_soln()
    
    
