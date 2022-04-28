# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 19:46:23 2022

@author: doujialiang

    It's GEOG5995 assignment1 sheep eat grass, wolves eat sheep
    uploaded on github: DOPrograme.github.io 
"""

import random

def distance_between(firstagent, secondagent): #uses trigonometry to determine distance between two agents (used for sharing and hunting)
    return (((firstagent.x - secondagent.x)**2) + ((firstagent.y - secondagent.y)**2))**0.5

class Agent:
# create object sheep    
    def __init__(self,environment,sheep,y=None,x=None):
       
        self.sheep=sheep
        self.environment=environment
        #sheep's orignal energy
        self.store=0
        # random x coordinate and () is the range of sheep's action
        self.x=random.randint(0,100)
        self.y=random.randint(0,100)
        # self.x=random.randint(0,len(environment))
        # self.y=random.randint(0,len(environment[0]))


    def move(self, boundary_y, boundary_x):
        
        if random.random() < 0.5 and self.x < boundary_x-2: #move coordinate by 5
            self.x=(self.x+1)%100
                
        else:
            if self.x > boundary_y+2:
                self.x=(self.x-1)%100
                  
        if random.random() < 0.5 and self.y < boundary_x-2:
            self.y=(self.y+1)%100
                   
        else:
            if self.y > boundary_y+2:
                self.y=(self.y-1)%100
    


    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 20:
            self.environment[self.y][self.x] -= 20
            self.store += 20
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = self.environment[self.y][self.x]-self.environment[self.y][self.x]
        


            
    # def distance_between(self, agent):
    #     return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    

        
    def share_with_neighbours(self, neighbourhood):
        for agent in self.sheep:
            if agent != self:            
                dist = distance_between(self,agent)
                if dist <= neighbourhood:
                    sum = self.store + agent.store
                    ave = sum /2
                    self.store = ave
                    agent.store = ave
                
    # def __str__(self):
    #     return (str(self.x) + "," + str(self.y) + "stores " + str(self.store))
    
class NearestSheep: #create for showing the nearest sheep coordinates from wolves
    def __init__(self, x, y, distance):
        self.distance = distance #distance between sheep and wolf
        self.x = x #the nearest sheeps x coordinate 
        self.y = y 
    
class Wolves(Agent):
    
    def __init__(self, environment,prey):
        self.prey=prey # list of interacting sheep, the data in it as same as Agent.sheep
        #self.wolves=wolves
        self.environment=environment
        self.x=random.randint(0,100)
        self.y=random.randint(0,100)

            
    def move(self,closest,speed,targets):
        trace=[]# create a list for tracking data
        #closest = MaxBoundary
        for agent in self.prey:
            trace.append(NearestSheep(agent.x, agent.y, distance_between(self, agent)))
        for i in range(targets): 
            if trace[i].distance < closest: #if this sheep is closer than the previous closest sheep
                closest = trace[i].distance #set this as the shortest distance to a sheep
        for i in range(targets):
            if closest == trace[i].distance: #if this sheep is the closest
                if self.x + speed < trace[i].x: #if full speed wont allow the wolf x coord to increase enough往最近的那个羊去移动
                    self.x += speed #increase x coordinate by max wolf movement
                else:
                    if self.x - speed > trace[i].x: #if full speed wont allow the wolf x coord to decrease enough
                        self.x -= speed #decrease x coordinate by wolf full speed
                    else:
                        self.x = trace[i].x #wolf must be within reach of sheep so move into sheep coordinates
            if closest == trace[i].distance: #repeats move conditions for y coordinates
                if self.y + speed < trace[i].y:
                    self.y += speed
                else:
                    if self.y - speed > trace[i].y:
                        self.y -= speed
                    else:
                        self.y = trace[i].y       

        # if random.random() < 0.5:
        #     self.x=(self.x+5)%100#speed=5
                
        # else:
        #     self.x=(self.x-5)%100
                
        
        # if random.random() < 0.5:
        #     self.y=(self.y+5)%100
                   
        # else:
        #     self.y=(self.y-5)%100
        
        
 
    
    # def bite(self, neighbourhoods):
    #     dead_sheep=[]
    #     for agent in self.sheep:
    #         dist = self.distance_between(agent)
    #         if dist<=neighbourhood:
    #             dead_sheep.append(agent)
    #     return dead_sheep
        
        

       
        