#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 12:37:00 2020

@author: nsbhatta
"""


"""
Perform Run Length Encoding compression on a string.


Your task is to compress a UTF-8 str to bytes using Run Length Encoding (RLE), a relatively straightforward compression scheme that takes any continuous run of 1 or more of the same byte and compresses it into two bytes, the first being the length of the run and the second being the byte itself.

We expect you to define a function compress that takes a single argument which is a UTF-8 str and returns a single even-length bytes value. Since individual UTF-8 characters can be more than one byte long you should encode the str to bytes before applying the RLE compression. For the purposes of this task you can assume that no run will ever be more than 255 bytes long, so no run will ever require more than one byte to encode.

For example:
>>> compress("abbcccddddaaaaaa")
b'\x01a\x02b\x03c\x04d\x06a'    
"""

import string
def compress(raw: str) -> bytes:
	#pass
	"""
	Logic:
	* loop through the encoded byte
	* for each char in the byte object:
			if current char != next char create the encoded object 
			else move to the next char (and increment by 1)
	* return the encoded object		
	"""
	
	bs = raw.encode("utf-8")
	benc = bytes()
	bcnt=1
	
	if not (raw):
		return benc # return empty byte object
	else:
		pass
		for i in range(len(bs)): # looping through the string
			try: # just to handle Indexerror for the last char of the string
				if bs[i]!=bs[i+1]:
					
					"""
					if char is ascii, encode to utf, while nonascii to latin-1 
					(the last test with multi byte was most painful as I had very little knowledge about bytes )
					# using a ternary operator
					"""
					val = chr(bs[i]).encode('utf-8') if 0 <= bs[i] <= 127 else chr(bs[i]).encode('latin-1')
					
					# convert count to byte and add it to val to generate the format as given in the question
					benc += bytes([bcnt]) + val
					bcnt = 1
				else:
					bcnt +=1
			except IndexError:
				val = chr(bs[i]).encode('utf-8') if 0 <= bs[i] <= 127 else chr(bs[i]).encode('latin-1')
				benc += bytes([bcnt]) + val
				
	return benc	
		
		
		
print(compress(""))
print(compress("a"))
print(compress("ab"))
print(compress("abbccc"))
print(compress("0"))
print(compress("011222"))
print(compress("a0bb11ccc222"))
print(compress("a" + "b" * 255 + "c"))
print(compress("a" * 255 + "0" * 255 + "b" * 255))
print(compress(string.ascii_letters))
print(compress(string.digits))
print(compress(string.punctuation))
print(compress(string.printable))
print(compress('😀 ☘'))

