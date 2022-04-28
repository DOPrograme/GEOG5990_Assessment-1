# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:26:45 2022

@author: doujialiang
"""

import random

import operator

import matplotlib.pyplot

agents=[] #new empty list

#y0=1;x0=1 #coordinates
y0=random.randint(0, 99)
x0=random.randint(0, 99)

agents.append([y0,x0])
agents.append([random.randint(0, 99),random.randint(0, 99)]) #same list
agents.append([random.randint(0, 99),random.randint(0, 99)])

print(agents)

print(max(agents))

print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1], agents[0][0])
matplotlib.pyplot.scatter(agents[1][1], agents[1][0])
matplotlib.pyplot.show()




