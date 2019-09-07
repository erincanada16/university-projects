# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:21:43 2019

@author: Erin Canada

Project # 2 is to implement linear regression for binary classification 
from scratch (as we've been discussing / working on for the past several 
lectures). Minimize the logistic regression objective function in two 
different ways: 1) using gradient descent; 2) using stochastic gradient descent.  
To evaluate the performance of your gradient descent implementation, make a 
semilogy plot of objective function value versus iteration. To evaluate the 
performance of your stochastic gradient descent implementation, make a 
semilogy plot of the objective function value versus epoch. You can use 
the plt.title() function to give the plots informative titles.

Train your logistic regression model on the same synthetic data that 
was used for the Perceptron project (project 1), and visualize the 
evolution of the decision boundary (which is a straight line) in the same 
way as was done for the Perceptron algorithm. We should observe that the 
decision boundary converges to a line that does a good job of separating 
the positive and negative training examples.

Submit just a .py file that contains your code -- set up the code so that
 when I run your Python program, the evolution of the decision boundary is 
 visualized, and the two semilogy plots are created.
 
"""

import numpy as np

import matplotlib.pyplot as plt

#log likelihood of the Logisitic Regression of Beta
def evalF(B,X,Y):
    
    N = X.shape[0]
    L = 0
    for i in range(N):
       L = Y[i]*np.log(sigmoid(X[i],B)) + (1-Y[i])*np.log(1-sigmoid(X[i],B))
    
    return -L
    
#Gradient of the Logistic Regression log liklihood        
def evalGrad(B,X,Y):
    
    N = X.shape[0]
    grad = 0
    for i in range(N):
        grad = grad + X[i]*(Y[i]- sigmoid(X[i],B))
        
    return -grad
    
    
 #Stochastic Gradient of the Logistic Regression   
def evalStoGrad(B,X,Y,idx):
    
    stoGrad = X[idx]*(Y[idx]- sigmoid(X[idx],B))
        
    return -stoGrad

#Generate Random data
def generateData():
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
    X = np.concatenate((Xpos,Xneg),axis = 0)
    return X

#Function for plotting a semilogy graph, pertaining to above functions
def semigraph(title, iteration, beta,lim):
    plt.grid(True, which="both")
    plt.semilogy(iteration, beta)
    plt.xlim(0,lim)
    plt.title('Logistic Regression w/ {}'.format(title))
    plt.xlabel('Iteration')
    plt.ylabel('Objective Function')
    plt.show()
    
#Prediction Function. Determines if data point should be classified as a 1 or zero
def sigmoid(X,B):
    
    r = np.dot(X.T,B)
    bottom = 1 + np.exp(-r)
    
    sig = 1/bottom
    
    return sig

 #Plot line to determine decision boundary   
def plotLine(B,xMin,xMax,yMin,yMax):
    
    xVals = np.linspace(xMin,xMax,100)
    yVals = (-B[0]*xVals - B[2])/B[1]
    
    idxs = \
        np.where((yVals >= yMin) & (yVals <= yMax))
    
    plt.plot(xVals[idxs],yVals[idxs])
    
    


        


   
   
#Compute Binary Logistic Regression with Gradient Descent
#Plot semilogy plot of objective function value vs iteration
#Training Data       
X = generateData()
N = X.shape[0]  

#Weights   
B = np.random.rand(3)

#Classification Vector
Y = np.zeros((N,1))

#Setting Classification Vector
for i in range(N):
    if sigmoid(X[i],B) > 0.5:
        Y[i] = 1
 
#Cost and iteration will be for the semigraph() function. bound will be for computing boundary line
cost = []
iteration = []
bound = []
t = 0.01
approx = 2000
for i in range(approx):
     B = B - (t*evalGrad(B,X,Y))
     b = evalF(B,X,Y)
     
     bound.append(B)
     cost.append(b)
     iteration.append(i)
     
 #Seeing the convergence to zero through numbers
    ##    if i % 5 == 0:
         
 ##        print("Iteration: " + str(i) + " Cost: " + str(b))
  
    
#Setting Graph Window and setting variables for graph
xMin = -3.0
xMax = 3.0
yMin = -3.0
yMax = 3.0

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


#Compute Binary Logistic Regression with Stochastic Gradient Descent
#Plot Semilogy plot of objective function vs epoch

X = generateData()
N = X.shape[0]  

#Weights   
B = np.random.rand(3)

#Classification Vector
Y = np.zeros((N,1))

#Setting Classification Vector
for i in range(N):
    if sigmoid(X[i],B) > 0.5:
        Y[i] = 1

#C and p are similar to cost and iteration for stochastic gradient descent graphs   
c = []
p = []
t = 0.01

    
num_epoch = 100
#Setting B1 = to B to not confuse two graphs
B1 = B
for epoch in range(num_epoch):
    idx = np.random.permutation(N)
    for idx in range(N):
        B1 = B1 - (t*evalStoGrad(B1,X,Y,idx))
    beta = evalF(B1,X,Y)
    p.append(beta)
    c.append(epoch)
    
 ##   if epoch % 10 == 0:
   ##     print("Iteration: " + str(epoch) + " Cost: " + str(p[epoch]))     
     
     
#Decision Boundary Graph
plt.figure()
plt.scatter(Xpos[:,0],Xpos[:,1])
plt.scatter(Xneg[:,0],Xneg[:,1])
for i in range(len(cost)):
    if i % 100 == 0:
        plotLine(bound[i],xMin,xMax,yMin,yMax)
plt.axis("equal") 
plt.show()

#Semilogy for Gradient Descent
plt.figure()
title1 = "Gradient Descent"
semigraph(title1,iteration, cost,approx)

#Semilogy for Stochastic Gradient Descent
plt.figure()    
title2 = "Stochastic Gradient Descent"
semigraph(title2,c,p,num_epoch)
    












