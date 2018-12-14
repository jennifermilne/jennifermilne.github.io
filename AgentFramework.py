# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:44:30 2018

@author: gy15j2m
"""
import random

##############################################################################
## Creating a class which defines the individual agents and their attributes##
##############################################################################

class Agent():
    def __init__ (self, environment,agents, x, y):
        #self._x = random.randint(0,299)
        #self._y = random.randint(0,299)
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y
        self.environment = environment
        self.agents = agents
        self.random_seed = 1
        self.store = 0

##############################################################################
############## A function for getting the attribute value of _x ##############
##############################################################################
    def getx(self):
        return self._x

##############################################################################
########## A function for setting the attribute value of _x ##################
##############################################################################
    def setx(self, value):
        self._x = value

##############################################################################
######### A function for deleting the attribute value of _x ##################
##############################################################################
    def delx(self):
        del self._x


    #x = property(getx, setx, delx, "I'm the 'x' property.")
    
##############################################################################
############## A function for getting the attribute value of _y ##############
##############################################################################
    def gety(self):
        return self._y

##############################################################################
########## A function for setting the attribute value of _y ##################
##############################################################################
    def sety(self, value):
        self._y = value

##############################################################################
######### A function for deleting the attribute value of _y ##################
##############################################################################
    def dely(self):
        del self._y
 
    #y = property(gety, sety, dely, "I'm the 'y' property.")               

##############################################################################
############### Move the agents randomly on a 300x300 graph ##################
##############################################################################
    def move(self):
        if random.random() < 0.5:
            self._x = (self._x + 1) % 300
        else:
            self._x = (self._x - 1) % 300
        
        if random.random() < 0.5:
            self._y = (self._y + 1) % 300
        else:
            self._y = (self._y - 1) % 300

##############################################################################
################## Get the agents to eat the environment #####################
##############################################################################
    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10

##############################################################################
### Get the agnets to share what they have eaten by two when they meet #######
### Input - neighbourhood                                              #######
### ##########################################################################
# Loop through the agents in self.agents .
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
# Calculate the distance between self and the current other agent:
            dist = self.distance_between(agent) 
# If distance is less than or equal to the neighbourhood
        if dist <= neighbourhood:
        # Sum self.store and agent.store .
            sum = self.store + agent.store
        # Divide sum by two to calculate average.
            ave = sum /2
        # self.store = average
            self.store = ave
            # agent.store = average
            agent.store = ave
#            print("sharing " + str(dist) + " " + str(ave))

##############################################################################
#### Calculating distance between two agents #################################
#### Input - agent                           #################################
#### Output - distance                       #################################
##############################################################################
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
    # End if
# End loop              
    