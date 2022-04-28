# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 16:30:24 2022

@author: doujialiang
"""

import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import csv
import agentframework

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) +
        ((agents_row_a[1] - agents_row_b[1])**2))**0.5



random.seed(0)


num_of_agents = 10
num_of_iterations = 10
neighbourhood = 20

agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#a = agentframework.Agent()
#b=agentframework.Agent()

#print(a)

#print(b)


f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

environment = []
for row in reader: # A list of rows
    rowlist = []    
    for value in row: # A list of value
        rowlist.append(value)
    environment.append(rowlist)
        
f.close() 
# Don't close until you are done with the reader;
# the data is read on request.




# Make the agents.
for i in range(num_of_agents):
#     agents.append([random.randint(0,99),random.randint(0,99)])
#     agents.append(agentframework.Agent(3,2))#这行代码更为简单的代替了上行代码，只需要在Agent里面写好
      agents.append(agentframework.Agent(i,environment,agents))
      # print(agents[i])
      
def update(frame_number):
    
    fig.clear()
    
    for i in range(num_of_iterations):
   
        
        
        agents[i].move()
        
        agents[i].eat()
        
        agents[i].share_with_neighbours(neighbourhood) 
        
        # print(agents[i])

        # if random.random() < 0.5:
        #     agents[i][0] = (agents[i][0] + 1) % 100
        # else:
        #     agents[i][0] = (agents[i][0] - 1) % 100

        # if random.random() < 0.5:
        #     agents[i][1] = (agents[i][1] + 1) % 100
        # else:
        #     agents[i][1] = (agents[i][1] - 1) % 100
    
    
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)

    matplotlib.pyplot.imshow(environment)

    # Move the agents.
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    matplotlib.pyplot.show()
    
    


    
#animation = matplotlib.animation.FuncAnimation(f,agents[i].move(),interval=1)
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)


# for agents_row_a in agents:
#     for agents_row_b in agents:
#         distance = distance_between(agents_row_a, agents_row_b)