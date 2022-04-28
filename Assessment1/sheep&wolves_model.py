# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:21:17 2022

@author: doujialiang
"""

import random
import operator
import Agent
import matplotlib.pyplot
import matplotlib.animation
import csv
import requests
import bs4
import tkinter
matplotlib.use('TkAgg')

boundary_x = 100 # Maximum extent of environment (Ensure this doesn't exceed boundaries of enviroment file (i.e. do not increase beyond 299 or decrease below 0))
boundary_y = 0
num_of_sheep = 20
num_of_wolves=2
num_of_iterations = 100
neighbourhood = 20
wolfspeed = 2 

#Set up required empty lists
environment = [] # a list defined by in.txt. 
sheep = [] # a list of agents defined by Agent.py
wolves=[]

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# read environment data as grass
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader: # A list of rows make cvs file into it
    rowlist = []    
    for value in row: # A list of value
        rowlist.append(value)
    environment.append(rowlist)
f.close() 



r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs) 

# Create Agent
for i in range(num_of_sheep):
    y=int(td_ys[i].text)
    x=int(td_xs[i].text)
    sheep.append(Agent.Agent(environment, sheep,y,x))

# Create Wolves
for i in range(num_of_wolves):
    wolves.append(Agent.Wolves(environment,sheep))

print("We have 20 sheep and 2 wolves")
# for i in range(10):
#     print(sheep[0].sheep[i].x, sheep[0].sheep[i].y, wolves[0].wolves[i].x)

def kill(self, sheep):
    global num_of_sheep 
    for agent in self.prey: #For every sheep
        if agent.x == self.x and agent.y == self.y: # If this sheep shares a space with the wolf
            sheep.remove(agent) # remove sheep from sheep list
            num_of_sheep -=  1 # reduce sheep count by one
            print("Sheep Eaten!") # notification of successful kill
            if num_of_sheep == 0:
                print ("All sheep eaten!!!")

def update(self):
    
    fig.clear()
    
    for i in range(num_of_sheep):

        sheep[i].eat()

        sheep[i].move(boundary_y, boundary_x)

        sheep[i].share_with_neighbours(neighbourhood) 

    for i in range(num_of_wolves):    
 
        wolves[i].move(boundary_x,wolfspeed,num_of_sheep)

        kill(wolves[i], sheep)
    

    for i in range(num_of_sheep):
    #for k in range(num_of_agents): #For every sheep
        for j in range(num_of_wolves):
        #for z in range(pack_size): #And every wolf
            matplotlib.pyplot.ylim(0, 100)#整个内容展示的大小
            #matplotlib.pyplot.ylim(MinBound, MaxBound) #limit y axis to environment
            matplotlib.pyplot.xlim(0, 100)
            #matplotlib.pyplot.xlim(MinBound, MaxBound) #limit x axis to environment
            matplotlib.pyplot.imshow(environment)
            #matplotlib.pyplot.imshow(environment, alpha=0.8) #plot environment
            matplotlib.pyplot.scatter(sheep[i].x,sheep[i].y,c="snow")
            #matplotlib.pyplot.scatter(agents[k].x,agents[k].y, color = "white") #plot the sheep
            matplotlib.pyplot.scatter(wolves[j].x,wolves[j].y,c="red")
            #matplotlib.pyplot.scatter(wolves[z].x, wolves[z].y, color = "red") #plot the wolf
    

    
# matplotlib.pyplot.ylim(0,299)
# matplotlib.pyplot.xlim(0,299)
# # matplotlib.pyplot.imshow(environment)

def run(): #Function for generating animation
   animation = matplotlib.animation.FuncAnimation(fig, update, frames=200, repeat=False)
   #animation = matplotlib.animation.FuncAnimation(fig, sim, frames=10, repeat=False)
   canvas.draw()
        
def Stop(): # function for stopping the model at it's defined conclusion
    global root
    root.quit()
    print('Model Completed!')
    
def terminate():  # Function to force quit model
    global root
    root.quit()
    root.destroy()

root = tkinter.Tk()    
root.wm_title("Sheep_Wolves Model") #Set title

#Create canvas for drawing model
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Create buttons which can call functions. 
run_button = tkinter.Button(root, text="Run Model", command=run) #button to start model
quit_button = tkinter.Button(root, text="Stop Model", command=terminate) #button to stop model
run_button.configure(bg='green') #colours start button green
quit_button.configure(bg='red') #colours stop button red
quit_button.pack(side=tkinter.BOTTOM) #locates stop button at bottom of gui
run_button.pack(side=tkinter.BOTTOM) #locates start button at bottom of gui


tkinter.mainloop() #load up GUI   

# animation = matplotlib.animation.FuncAnimation(fig, update, interval=1000,repeat=False, frames=num_of_iterations)  

    
# matplotlib.pyplot.show()
    
    
    
    
    