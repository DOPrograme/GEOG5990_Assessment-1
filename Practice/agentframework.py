# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:56:51 2022

@author: doujialiang
"""
import random



class Agent:
    
    def __init__(self,ia,environment,agents):#self.x跟x不是一个东西
        #self.x=x
        self.id=ia
        self.x=random.randint(0,99)
        # self.x=x
        #self.y=y
        self.y=random.randint(0,99)
        # self.z=random.randint(0,99)
        #print(agents[i])
        
        self.environment = environment
        self.store = 0
        
        self.agents=agents
       

    
    def __str__(self):
       return "id="+ str(self.id)+",y="+ str(self.y)+",x=" + str(self.x)
    
    def move(self):#没有__不是内部函数
        
        for i in range(10):
            if random.random() < 0.5:
                self.x=(self.x+1)%100
                
            else:
                self.x=(self.x-1)%100
                  
        
            if random.random() < 0.5:
                self.y=(self.y+1)%100
                   
            else:
                self.y=(self.y-1)%100
            
    # def move_coordinate:
    
   
    
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10 
            
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(dist) + " " + str(ave))

 


    
    
    
        
  
        
    
               
  

    
