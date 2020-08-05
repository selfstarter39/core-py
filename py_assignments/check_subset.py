#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 23:00:03 2020

@author: nsbhatta

https://www.hackerrank.com/challenges/py-check-subset/problem

You are given two sets, A and B.
Your job is to find whether set  is a subset of set .

If set A is subset of set B, print True.
If set A is not a subset of set B , print False.

Input Format

The first line will contain the number of test cases,T .
The first line of each test case contains the number of elements in set A .
The second line of each test case contains the space separated elements of set A .
The third line of each test case contains the number of elements in set B .
The fourth line of each test case contains the space separated elements of set B.

Constraints
* 0 < T < 21
* 0 < Number of elements in each set < 1001

Output Format

Output True or False for each test case on separate lines.

Sample Input:
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

Sample Output
True 
False
False
"""


def chk_subset():
    dct={}
    try:
        t = int(input())
        
        if 0<t<21:
            for i in range(t):
                e_setA = int(input())
                elmA = input()
                e_setB = int(input())
                elmB = input()
                
                elm_A_lst = [int(val) for val in elmA.split(" ")]
                elm_B_lst = [int(val) for val in elmB.split(" ")]

                
                if (len(elm_A_lst) == e_setA) and (len(elm_B_lst) == e_setB) and (0<len(elm_A_lst)<1001) and (0<len(elm_B_lst)<1001):                    
                    
                    dct[i] = set(elm_A_lst).issubset(set(elm_B_lst))

                else:
                    print("Inout err")
                    return None
  
        else:
            print("Test case cnt err")
            return None
        
    
        gen_exp = (vals for vals in dct.values())
        for vals in gen_exp:
            yield vals
    
    except ValueError:
        print("ValErr")
        return None
    
    

    
    
for i in chk_subset():
    print(i)