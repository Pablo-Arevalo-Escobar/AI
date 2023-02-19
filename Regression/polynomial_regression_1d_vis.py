#!/usr/bin/env python
# coding: utf-8

# It is difficult to visualize the results of high-dimensional regression. Instead, only use one
# of the features (use the 3rd feature, i.e. X n[:,2] since Python index starts with 0) and
# again perform polynomial regression. Produce plots of the training data points, learned
# polynomial, and test data points. The code visualize 1d.py may be useful. Put 2 or
# 3 of these plots, for interesting (low-order, high-order) results, in your report.
# Include brief comments.

# In[1]:


import numpy as np
from scipy.io import *
import matplotlib.pyplot as plt


# #### Utility

# In[2]:


def loadData():
    data = np.loadtxt('auto-mpg.data', usecols=(0,1,2,3,4,5,6,7))
    t = data[:,0]
    X = data[:,1:]
    rp = np.squeeze(loadmat('rp.mat')['rp']-1)
    X = X[rp,:]
    t = t[rp]
    return t,X

def degexpand(X,k):
    (n,d) = X.shape

    P = np.ones((n,1))
    for i in range(k):
        P = np.hstack((P,X**(i+1)))

    return P

def normalizeData(X):
    N = X.shape[0]
    mu = np.mean(X,axis=0)
    sig = np.std(X,axis=0)
    
    X = (X - mu) / sig # python broadcasting
    return X


# In[3]:


[t,X] = loadData()
X = normalizeData(X)
t = normalizeData(t)
# This type of slicing is necessary for the data to 
# be formatted in a way that degexpand can work with it
X_3 = X[:,2:3] 
X_train = X_3[0:100,:]
X_test = X_3[101:,:]
t_train = t[0:100]
t_test  = t[101:]


# In[4]:


def poly_regression(P,t):
    W_brackets = np.linalg.inv(np.dot(P.T,P))
    W_P = np.dot(W_brackets, P.T)
    W_ml = np.dot(W_P,t)
    return W_ml

def squared_error(X,w,t):
    Xw_min_t = (X.dot(w) - t)
    return (0.5*np.dot(Xw_min_t.T,Xw_min_t))

def learned_polynomial(X,w):
    return X.dot(w)


# In[5]:


#Plot data spread
fig, axs = plt.subplots(1)
fig.set_figwidth(15)
fig.set_figheight(5)
fig.suptitle("Data spread and learned polynomial")
plt.xlim([-2,4])
plt.ylim([-2,5])
#Plot data
axs.plot(X_train, t_train, 'b.', ms = 10, label = "Training data")
axs.plot(X_test,t_test, 'r.', ms = 8, label = "Testing data")
axs.legend()


# In[7]:


degrees = [1,6,15] 

#Plot parameters
fig, axs = plt.subplots(3)
fig.set_figwidth(15)
fig.set_figheight(15)
plt.xlim([-2,4])
plt.ylim([-2,5])


#Prepare X axis
ev = np.arange(min(X_3), max(X_3) + 0.1, 0.1)
x_ev = np.ones((ev.shape[0],1))


for i in range(0,3):
    #Compute W
    deg = degrees[i]
    P_train = degexpand(X_train,deg)
    P_test =  degexpand(X_test,deg)
    W_ml = poly_regression(P_train,t_train) 

    #Compute polynomial
    x_ev[:,0] = ev
    x_ev_expanded = degexpand(x_ev,deg)
    poly_x = learned_polynomial(x_ev_expanded, W_ml)
    
    #Plot
    axs[i].set_title("Learned Polynomial at M = {}".format(deg))
    axs[i].set(xlim = (-2,4), ylim=(-2,5))
    axs[i].plot(X_train, t_train, 'b.',markerfacecolor = 'none', ms = 6, label = "Training data")
    axs[i].plot(X_test, t_test, 'r.', ms = 6,markerfacecolor = 'none', label = "Testing data")
    axs[i].plot(x_ev, poly_x, 'g.-', ms = 15, label = "Polynomial")
    axs[i].legend()




plt.show()

