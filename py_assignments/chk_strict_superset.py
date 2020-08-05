#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 08:48:59 2020

@author: nsbhatta

https://www.hackerrank.com/challenges/py-check-strict-superset


You are given a set A and  other n sets.
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Sample Input 0

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

Sample Output 0
False

Logic used:
* Check if N is a subset of A and len(A-N) > 0
"""


def supr_subset():
    prevflag = False
    curflag =False
    finalflag = False
    inputchk = 1
    
    
    try:
        a = input()
        suprst = [val for val in a.split(" ")]
        if 0<len(suprst)<501:
            n = int(input())
            if 0<n<21:
                for i in range(n):
                    #print(f"Test case: {i}")
                    #print("-----------------")
                    n = input()
                    nset = [element for element in n.split(" ")]
                    if 0<len(nset)<101:
                        
                        flag1 = set(nset).issubset(set(suprst))
                        flag2 = len(set(suprst) - set(nset))
                        
                        #print(flag1)
                        #print(flag2)
                        if (flag1) and (flag2 > 0):
                            curflag = True
                            #print(curflag)
                        else:
                            curflag = False
                            #print(curflag)
                            
                        if i ==0:
                            prevflag = curflag
                            finalflag = prevflag and curflag
                            #print("Final flag:",finalflag)
                            
                        else:
                            finalflag = prevflag and curflag
                            #print("Final flag:",finalflag)
                            prevflag = curflag
                            
                            
                            
                    else:
                        inputchk = 0
            
            else:
                inputchk = 0
            
        else:
             inputchk = 0
         
        
        # Final return block
        """
        if not inputchk:
            return  finalflag
        """

    except ValueError:
        #print("In except")
        #print("Flag :",finalflag)
        return None

    if inputchk :
        return  finalflag
    else:
        return None


print(supr_subset())

    