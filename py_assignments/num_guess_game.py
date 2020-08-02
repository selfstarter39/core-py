#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 23:02:27 2020

@author: nsbhatta


For this exercise

* Write a function (guessing_game) that takes no arguments.

* When run, the function chooses a random integer between 0 and 100 (inclusive).

* Then ask the user to guess what number has been chosen.

* Each time the user enters a guess, the program indicates one of the following:

- Too high

- Too low

- Just right

* If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.

* The program only exits after the user guesses correctly.

"""

import random
def num_guess():
    rand_num = random.randint(0,10)
    
    while (1<2):
        try: # try block is used to handle inout errors like  strings:"Hi" or empty inputs:""
            usr_num = int(input("Guess the number: "))
            if usr_num == rand_num:
                print("Just right")
                break
            elif usr_num > rand_num:
                print("Too high")
                
            else:
                print("Too low")
                
        except  ValueError:
            continue
            
                
            
num_guess()            