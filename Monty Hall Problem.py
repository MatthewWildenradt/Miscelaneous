#!/usr/bin/env python
# coding: utf-8

# In[1]:


#as always, import what we need
import numpy as np
import matplotlib.pyplot as plt

#function to make random door indexes
def randomDoorIndex(doors):
    randomDoorIndex=int((len(doors))*np.random.random())
    return randomDoorIndex

#function to make doors and assign a prize door and a picked door
def doorCreator(numberOfDoors):
    doors=np.zeros(numberOfDoors)
    carIndex=randomDoorIndex(doors)
    pickedDoor=randomDoorIndex(doors)
    return doors, carIndex, pickedDoor

#function to pick a door index != pickedDoor
def unpickedDoorPicker(doors, pickedDoor):
    while True:
        possibleDoor=randomDoorIndex(doors)
        if possibleDoor!=pickedDoor:
            return possibleDoor
            break
            
#function to generate the alternate door
def alternateDoorGenerator(doors, carIndex, pickedDoor):
    if carIndex!=pickedDoor:
        unpickedDoor=carIndex
        return unpickedDoor
    else:
        unpickedDoor=unpickedDoorPicker(doors, pickedDoor)
        return unpickedDoor
               
#function returns true of the contestant wins by switching doors
def finalDoorPicker(pickedDoor, carIndex):
    if pickedDoor!=carIndex:
        return True
    else:
        return False
    
#now let's make a function to bring all those functions together
def montyMethod(numberOfDoors):
    doors, carIndex, pickedDoor=doorCreator(numberOfDoors)
    unpickedDoor=alternateDoorGenerator(doors, carIndex, pickedDoor)
    result = finalDoorPicker(pickedDoor, carIndex)
    return result

#now let's make a monte-carlo simulation based on that function above
def monteCarloMethod(numberOfDoors, N):    
    switchWinCount=0
    stayWinCount=0
    for i in range(N):
        result=montyMethod(numberOfDoors)
        if result:
            switchWinCount=switchWinCount+1
        else:
            stayWinCount=stayWinCount+1
    return switchWinCount/N, stayWinCount/N

#function to display the estimated probability based on monteCarloMethod
def printMonteCarlo(numberOfDoors, N):
    switchProb, stayProb=monteCarloMethod(numberOfDoors, N)
    return switchProb, stayProb

#a little function to make sure all x axis ticks are integers
def xAxisInt():
    ax=plt.gca()
    x_ax=plt.gca().get_xticks()
    for i in range(len(x_ax)):
        x_ax[i]=int(x_ax[i])
    ax.set_xticklabels(x_ax)
    
#function to graph reuslts of the monteCarloMethod using different values for N
#numberOfDoors must be >= 3
def graphMonteCarloTrials(numberOfDoors, N):
    numberOfSimulations=np.arange(1,N+1,1)
    switchProbResults=np.zeros(N)
    stayProbResults=np.zeros(N)
    for i in numberOfSimulations:
        switchProbResults[i-1], stayProbResults[i-1]=monteCarloMethod(numberOfDoors, i)
    plt.plot(numberOfSimulations, switchProbResults, 'g', label="switch")
    plt.plot(numberOfSimulations, stayProbResults, 'r', label="stay")
    plt.title("Accuracy Based on # of Trials"+" (number of doors = "+str(numberOfDoors)+")", size=12, weight='bold')
    plt.xlabel("# of monte-carlo trials") 
    plt.ylabel("% of correct door picks") 
    plt.legend()
    xAxisInt()
    
#function to graph reuslts of the monteCarloMethod using different values for numberOfDoors
#numberOfDoors must be >= 3
def graphMonteCarloDoors(numberOfDoors, N):
    numbersOfDoors=np.arange(3,numberOfDoors+1,1)
    switchProbResults=np.zeros(numberOfDoors-2)
    stayProbResults=np.zeros(numberOfDoors-2)
    for i in numbersOfDoors:
        switchProbResults[i-3], stayProbResults[i-3]=monteCarloMethod(i, N)
    plt.plot(numbersOfDoors, switchProbResults, 'g', label="switch")
    plt.plot(numbersOfDoors, stayProbResults, 'r', label="stay")
    plt.title("Accuracy Based on # of Doors"+" (# of Trials = "+str(N)+")", size=12, weight='bold')
    plt.xlabel("# of doors at beginning") 
    plt.ylabel("% of correct door picks")
    plt.legend()
    xAxisInt()
    
#now let's make a function to plot both graphMonteCarloTrials() and graphMonteCarloDoors() at once
#can take separate arguments for each graph but defaults to the same
def montyHallGraph(numberOfDoors, N, numberOfDoors2=None, N2=None):
    if numberOfDoors2 is None and N2 is None:
        numberOfDoors2=numberOfDoors
        N2=N
    plt.subplot(2, 1, 1); graphMonteCarloTrials(numberOfDoors, N)
    plt.subplot(2, 1, 2); graphMonteCarloDoors(numberOfDoors2, N2)
    plt.subplots_adjust(hspace = 0.7)


# In[6]:


montyHallGraph(100, 100)


# In[ ]:




