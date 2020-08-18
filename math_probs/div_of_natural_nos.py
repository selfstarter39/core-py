#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 22:47:43 2020

@author: nsbhatta

Find all divisors of a natural number

E.g: 50 
1 2 5 10 25 50
"""

import math

def brute_force_soln():
    """
    * Arguments : None
    * Number is taken as input
        * Loop through the range of number
        * Divide by each item 
        * if remainder = 0, it is a factor

    Returns
    -------
    None.

    """
    
    try:
        n = int(input("Enter a number :"))
        print ("Solution via brute force..\n")
        for i in range(1,n+1):
            if n % i == 0:
                print(i, end =" ")
    except ValueError:
        return None
        
        
    return None


def faster_soln():
    """
    * Arguments : None
    * Number is taken as input
        * As observed, all the divisors are present in pairs. 
        * E.g.: if n = 100, then the pairs of divisors are: (1,100), (2,50), (4,25), (5,20), (10,10)
        * So we just need to grab each of these pairs
        * Special care shld be taken for squares (so that we don't repeat the numbers, e.g. 10 and 10; only 1 is to be considered)

    Returns
    -------
    None.

    """
    lst =[]
    try:
        n = int(input("Enter a number :"))
        print ("Faster soln..\n")
        for i in range(1,int(math.sqrt(n))+1):
            if n % i == 0:                
                lst.append(i)
                lst.append(n//i)
                
    except ValueError:
        return None
        
    for val in sorted(set(lst)):
        print(val, end=" ")
    return None
    
    
    

if __name__ == "__main__":
    #brute_force_soln()
    faster_soln()