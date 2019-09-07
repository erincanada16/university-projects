# -*- coding: utf-8 -*-
"""PCA_MNIST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z_uQM10zt5z-AZJPpbVtKMepzKZhCXIF

# PRINCIPAL COMPONENT ANALYSIS

Directions: Perform PCA (in Python) using the MNIST training images. 

Select a test image at random, and display the test image alongside the approximation to the test image that is obtained using the first 50 principal components.  How many principal components do you need in order for the approximation to the test image to look pretty good?

Also display the top 16 principal component vectors as images.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow 
from tensorflow.keras.datasets import mnist 
from tensorflow.keras import models 
from tensorflow.keras import layers

"""## Defining Functions"""

def pca_approx(X_train,train_idx,V,components):
  #computing approximation
  Xbar = np.mean(X_train,axis = 0)
  approximation = Xbar
  xi = X_train[train_idx]
  for i in range (components):
    vi = V[:,i]
    ci = np.vdot(xi-Xbar,vi)
    approximation = approximation + ci*vi
    
  xi = np.reshape(xi,(28,28))
  approximation = np.reshape(approximation,(28,28))

  #creating figure
  plt.figure()
  plt.imshow(xi, cmap='gray')
  plt.title("Actual")

  plt.figure()
  plt.imshow(approximation, cmap='gray')
  title = "Approximation with {} Components".format(components)
  plt.title(title)

"""## Loading Data"""

(X_train,Y_train), (X_test, Y_test) = mnist.load_data()

# Reshape and scale data:
X_train = X_train.reshape((60000, 28 * 28))
X_train = X_train.astype('float32')/255
X_train = X_train[0:5000]
X_test_orig = X_test.copy()
X_test = X_test.reshape((10000, 28 * 28))
X_test = X_test.astype('float32')/255


#One Hot Encoding
Y_train = tensorflow.keras.utils.to_categorical(Y_train)
Y_train = Y_train[0:5000]
Y_test = tensorflow.keras.utils.to_categorical(Y_test)

"""## Setting Variables"""

#Setting up variables, Y = X-Xbar
Xbar = np.mean(X_train,axis = 0)

A = X_train - Xbar

U, Sigma, VT = np.linalg.svd(A)
V = VT.T
S = np.zeros((5000,784))
S[0:784,0:784] = np.diag(Sigma) 

#Value really close to zero... check!
check = U@S@VT
diff=np.max(np.abs(A-check))

"""# Compute PCA"""

components = [1,20,50,100,500]
train_idx = np.random.randint(5000)
for i in range(len(components)):
  comp = components[i]
  pca_approx (X_train,train_idx,V,comp)

"""From comparing these images, it looks like 50 is a good amount of principle components to determine the image.

Top 16 Components
"""

idx = 1

for i in range(4):
  for j in range(4):
    vi = V[:,idx]
    vi = np.reshape(vi, (28,28))
    plt.subplot(4,4,idx)
    plt.imshow(vi,cmap = 'gray')
    idx = idx + 1