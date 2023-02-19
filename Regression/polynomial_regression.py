#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
from scipy.io import *
import matplotlib.pyplot as plt


# ### Utility Functions

# In[15]:


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


# ### Preprocessing the  Data

# In[16]:

[t,X] = loadData()
X = normalizeData(X)
t = normalizeData(t)
X_train = X[0:100,:]
X_test = X[101:,:]
t_train = t[0:100]
t_test  = t[101:]


# ### Training the  Data
# The code below is used to perform polynomial regression
#  - P_train and P_test lists containing the degree expanded version of each of their respective datasets
#  - W_ml is a list containing the respective weights for each polynomial degree 
#  - E_train and E_test contain the mean squared error at each degree

# In[17]:


def poly_regression(P,t):
    W_brackets = np.linalg.inv(np.dot(P.T,P))
    W_P = np.dot(W_brackets, P.T)
    W_ml = np.dot(W_P,t)
    return W_ml

def squared_error(X,w,t):
    Xw_min_t = (X.dot(w) - t)
    return (0.5*np.dot(Xw_min_t.T,Xw_min_t))


# In[18]:


poly_degree = [deg for deg in range(1,11)]

P_train = [degexpand(X_train,deg) for deg in poly_degree ]
P_test  = [degexpand(X_test,deg) for deg in poly_degree ]

W_ml = [poly_regression(P,t_train) for P in P_train]


# ### Testing and Plotting the Results

# In[19]:


E_train = [squared_error(P,W_ml[i],t_train) for i,P in enumerate(P_train) ]
E_test  = [squared_error(P,W_ml[i],t_test) for i,P in enumerate(P_test)]


# In[20]:


plt.yscale("log")

plt.xlabel("M")
plt.ylabel("Erms")
plt.plot(poly_degree, E_train, 'b.-', ms = 15, markerfacecolor = 'none',label = "train_error")
plt.plot(poly_degree, E_test,'r.-', ms = 15, markerfacecolor = 'none', label = "test_error" )
plt.legend()
plt.show


# %%
