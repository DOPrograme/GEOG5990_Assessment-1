# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 16:38:11 2022

@author: doujialiang
"""

a = 10.0 % 3
print(str(type(a)) + " " + str(a))

a = 5
if a < 10:
    print (a)
    print ('''done''')
    


import random

y0 = 50; x0 = 50


if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

print(y0, x0)


y1 = 50; x1 = 50

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y1, x1)

answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print(answer)