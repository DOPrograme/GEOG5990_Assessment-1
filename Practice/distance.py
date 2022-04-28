# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 16:48:33 2022

@author: doujialiang
"""

import random
import operator
import matplotlib.pyplot

num_of_agents = 10
num_of_iterations = 100
agents = []

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5  

# Make the agents.
for i in range(num_of_agents):#a for-loop, we can create as many agents as we like
    agents.append([random.randint(0,99),random.randint(0,99)])#This creates one new set of coordinates
    if i>=1:
        distance = distance_between(agents[i-1], agents[i])
        print(distance)




# Move the agents.
'''
This moves our coordinates twice. 
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
'''

for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents.append([random.randint(0,99),random.randint(0,99)])

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
answer = (((agents[i][0] - agents[i+1][0])**2) + ((agents[i][1] - agents[i+1][1])**2))**0.5
print(answer)



matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()