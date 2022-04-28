# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 19:46:23 2022

@author: doujialiang

    It's GEOG5995 assignment1 sheep eat grass, wolves eat sheep
    uploaded on github: DOPrograme.github.io 
"""

import random

class Animal:
    
    def _init_(self,environment,sheep,wolves):
        self.wolves=wolves
        self.sheep=sheep
        self.environment=environment
        self.x=random.randint(0,99)
        self.y=random.randint(0,99)