#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 19:13:21 2020

@author: nsbhatta
"""


def cart_prdt(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    reslist=[]
    flist = []
    ptup = [tuple(pool) for pool in args]*repeat
    print(ptup)
    
    for tups in ptup:
        #reslist = flist[:]
        if not reslist:
            for val in tups:
                reslist.append(val)
            
            #print("reslist with initial values: ", reslist)
            
        else:
            for ech in reslist:
                for val in tups:
                    nstr = str(ech) + str(val)
                    flist.append(nstr)
             
            #print("flist: ", flist)   
            reslist = flist[:]
            flist = []
            #print("reslist: ", reslist)  
                
    
    #print(len(reslist))
    for val in reslist:
        yield val        
 

## Code for cartesian product:
for c in cart_prdt("abc","xy"):
    print(c)
    
 
## Code for permutation of a string        
c = 0
for i in (cart_prdt('ABCD',repeat=4)):
    if len(set(i)) == 4:
        print(i)
        c+=1
print(c)        

