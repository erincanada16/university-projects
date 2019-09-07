# -*- coding: utf-8 -*-
"""classifyMNIST

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZxDo1ioXJTNLyIQdTlzXwiu2HqqYXK-a

# MNIST CLASSIFICATION WITH MULTICLASS LOGISTIC REGRESSION
"""

import pandas as pd
import matplotlib.pyplot as plt
import io
import numpy as np
import tensorflow 
from tensorflow.keras.datasets import mnist 
from tensorflow.keras import models 
from tensorflow.keras import layers

"""## SETTING UP Functions"""

def soft_max(X,Y,B):
    
    numExamples, numFeatures = X.shape
    numExamples, numClasses = Y.shape
    
    numerator = np.exp(X@B)
    denom = np.sum(numerator,axis =1) 
    denom = np.reshape(denom,(numExamples,1))  
    denom = np.tile(denom,(1,numClasses)) 
    p = numerator/denom
    
    return p
  
  

def eval_f(X,Y,B):
  f = np.sum(Y*np.log(soft_max(X,Y,B)))

  return -f

def eval_grad(X,Y,B):
    
    
    numExamples, numFeatures = X.shape
    numExamples, numClasses = Y.shape
    grad = np.zeros((numFeatures,numClasses))
    
    grad = X.T@(soft_max(X,Y,B) - Y)
    
    
    return grad

"""## SETTING UP VARIABLES"""

(X_train,Y_train), (X_test, Y_test) = mnist.load_data()



# Reshape and scale data:
X_train = X_train.reshape((60000, 28 * 28))
X_train = X_train.astype('float32')/255
#X_train = X_train[0:5000]
X_test_orig = X_test.copy()
X_test = X_test.reshape((10000, 28 * 28))
X_test = X_test.astype('float32')/255


#One Hot Encoding
Y_train = tensorflow.keras.utils.to_categorical(Y_train)
#Y_train = Y_train[0:5000]
Y_test = tensorflow.keras.utils.to_categorical(Y_test)

"""## MULTICLASS LOGISTIC REGRESSION ON MNIST DATA SET"""

#SET UP FOR GRADIENT DESCENT
maxIter = 1000
t = 0.00001
#SETTING UP VARIABLES
numExamples, numFeatures = X_train.shape
numExamples, numClasses = Y_train.shape


B = np.random.rand(numFeatures,numClasses)



#SETTING UP FOR SEMIOLOGY PLOT
costs = np.zeros(maxIter)
m_iter = np.zeros(maxIter)
#GRADIENT DESCENT FOR TRAIN DATA
for i in range(maxIter):
  B = B - (t*eval_grad(X_train,Y_train,B))
  cost = eval_f(X_train,Y_train,B)
  costs[i] = cost
  m_iter[i] = i
  
  if i%50 == 0:
    print(cost)

"""## Semiology Plot"""

#Semiology plot
plt.grid(True, which="both")
plt.semilogy(m_iter, costs)
plt.title('Multiclass Logistic Regression with MNIST dataset')
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.show()

"""## Predicting Test Data"""

#Set up predictons matrix
Y_final = np.zeros(Y_test.shape,dtype=int)
softmax = soft_max(X_test,Y_final,B)
#Assigning highest probability for prediction
for i in range(Y_final.shape[0]):
  argmax = np.argmax(softmax[i])
  Y_final[i][argmax] = 1

#PREDICTION ACCURACY
correct = 0
incorrect = 0

for i in range(Y_final.shape[0]):
  #print("Predicted: " + str(np.argmax(Y_final[i])) + " Actual: " + str(np.argmax(Y_test[i])))
  final = np.argmax(Y_final[i]) == np.argmax(Y_test[i])
  if (final):
    #print("Yay!")
    correct = correct + 1
  else:
    incorrect = incorrect + 1
    
accuracy = correct/(incorrect + correct)

print("Classification Accuracy: " + str(accuracy*100) + "%")