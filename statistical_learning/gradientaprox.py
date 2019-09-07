# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:56:18 2019

@author: Erin Canada
"""
import numpy as np

import matplotlib.pyplot as plt #plt.plot(x,y)


def logSumExp(x):
    n = len(x)
    s = 1.0
    for i in range(n):
        s = s + np.exp(x[i])
        
    return np.log(s)

def gradLogSumExp(x):
    n = len(x)
    s = 1.0
    grad = np.zeros(n)
    
    
    for i in range(n):
        s = s + np.exp(x[i])
        
    for i in range(n):
        grad[i] = np.exp([x[i]])/s
        
        return grad
  
    
def gradApprox(f,x,dx):
    
    # f is a function such as the logSumExp function.
    # x is a numpy array, e.g., x = np.random.randn(10)
    # dx is a small positive number such as .01
    # This function numerically approximates the gradient# of f at x.
    n = len (x)
    grad = np.zeros(n)
    
    for i in range(n):
       xP = x.copy()
       xP[i] = x[i] + dx
       xM = x.copy()
       xM[i] = x[i] - dx
    
        
       grad[i] = (f(xP) - f(xM))/2*dx
        
       return grad
    

x = 10*np.random.rand(5)
grad = gradLogSumExp(x)
dx = 0.0000001
norm = []
plot = []
count = 0

while dx <= 0.1:
    
    gradEst = gradApprox(logSumExp,x,dx)

    norm.append(np.linalg.norm(grad-gradEst))
    
    plot.append(dx)
    plot.append(norm[count])
    
    dx = dx*10
    count = count + 1
    
    
#Plot showing error in approximation 
figure, ax = plt.subplots(figsize=(5,3))
ax.set_title("Error in Approximation")
ax.set_ylabel("Error")
ax.set_xlabel("Value of dx")
ax.set_xlim(xmin = 0.0000001,xmax = 0.1)
ax.set_ylim(ymin = 0, ymax = 0.005)
plt.plot(plot)

"""
From doing this exercise, I noticed that the larger the dx, 
in this case 0.1, the larger the error.
"""