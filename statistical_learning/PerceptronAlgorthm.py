# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 13:14:32 2019
Perceptron Algorithm

@author: Erin Canada
"""

import numpy as np
import numpy.random
import matplotlib.pyplot as plt

def perceptron(Xpos,Xneg,t):
    
    #Set number of epochs or each pass through the data in a randomized order
    num_epoch = 50000
    
    

    #Stack Xpos and Xneg to make one training set
    X = np.concatenate((Xpos,Xneg),axis = 0)
    #Consider shape for boundaries
    numPos = Xpos.shape[0]
    numNeg = Xneg.shape[0]
    
    N = X.shape[0]
    
    #Setting up a starting 'a'
    a = np.random.rand(3)
    
    #For each epoch
    for epoch in range (num_epoch):
        idx = np.random.permutation(N)
        #Run through each X in a random order
        for i in idx:
            xi = X[i,:]
            #Case 1 
            #If the final output is positive
            if i < numPos:
                #And it was falsely classified as negative
                if np.vdot(a,xi) < 0:
                    #Adjust 'a'
                    a = a + t*xi
                
            #Case 2
            #If the final output is negative
            if i > numNeg:
                #And was falsely classified as positive
                if np.vdot(a,xi) > 0:
                    #Adjust 'a'
                    a = a - t*xi
                    
        
           
        #plot epoch
        if epoch % 500 == 0:
            xMin = -3.0
            xMax = 3.0
            yMin = -3.0
            yMax = 3.0

            #Plotting points 
            plt.clf() 
            plt.scatter(Xpos[:,0],Xpos[:,1])
            plt.scatter(Xneg[:,0],Xneg[:,1])
             
            plotLine(a,xMin,xMax,yMin,yMax)
            plt.axis("equal") 
            plt.pause(.05) 
    
    print("Hello from inside the perceptron function!")
    return 0

def plotLine(a,xMin,xMax,yMin,yMax):
    
    xVals = np.linspace(xMin,xMax,100)
    yVals = (-a[0]*xVals - a[2])/a[1]
    
    idxs = \
        np.where((yVals >= yMin) & (yVals <= yMax))
    
    plt.plot(xVals[idxs],yVals[idxs])
    
numPos = 100
numNeg = 100

np.random.seed(14)
muPos = [1.0,1.0]
covPos = np.array([[1.0,0.0],[0.0,1.0]])

muNeg = [-1.0,-1.0]
covNeg = np.array([[1.0,0.0],[0.0,1.0]])

Xpos = np.ones((numPos,3))
for i in range(numPos):
    Xpos[i,0:2] = \
        np.random.multivariate_normal(muPos,covPos)
        
Xneg = np.ones((numNeg,3))
for i in range(numNeg):
    Xneg[i,0:2] = \
        np.random.multivariate_normal(muNeg,covNeg)
        
a = np.random.randn(3)

xMin = -3.0
xMax = 3.0
yMin = -3.0
yMax = 3.0

plt.scatter(Xpos[:,0],Xpos[:,1])
plt.scatter(Xneg[:,0],Xneg[:,1])
plotLine(a,xMin,xMax,yMin,yMax)
plt.axis("equal") 
plt.pause(.05) 

t = .000001
a = perceptron(Xpos,Xneg,t)
