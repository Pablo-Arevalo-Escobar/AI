#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
from scipy.io import *
import matplotlib.pyplot as plt


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


# In[16]:


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


# In[17]:


def poly_ridge_regression(lam,P,t):
    #Computing the ridge regression estimate
    I = np.identity(P.shape[1])
    W_brackets = np.linalg.inv(np.dot(lam,I) + np.dot(P.T,P))
    W_P = np.dot(W_brackets, P.T)
    W_rr = np.dot(W_P, t)
    return W_rr

def squared_error_ridge(X,w,t, lam):
    Xw_min_t = (X.dot(w) - t)
    lambda_wTw = lam*np.dot(w.T, w)
    return (np.dot(Xw_min_t.T,Xw_min_t) + lambda_wTw)

def learned_polynomial(X,w):
    return X.dot(w)


# In[18]:


#Perfom 10-fold cross validation
def cross_validation10(lam):
    cv_set = [X_train[n:n+10] for n in range(0,100,10)]

    avg_error = 0
    for i in range(0,10):
        validation_set = cv_set[i]
        train_set = np.concatenate([data for ind,data in enumerate(cv_set) if ind != i])
        t_train_set = np.array([data for ind, data in enumerate(t_train) if (ind < i or ind > (i+9))])

        V = degexpand(validation_set,8)
        P = degexpand(train_set,8)

        #Train on 90% of training data
        W_rr = poly_ridge_regression(lam,P,t_train_set)

        #Validate on the other 10% of training data
        t_test_set = np.array(t_train[(i*10):(i*10)+10])
        avg_error += squared_error_ridge(V,W_rr,t_test_set, lam)
    avg_error /= 10
    return avg_error



# In[19]:


lam = [0,0.01,0.1,1,10,100,1000]
avg_errors = [cross_validation10(l) for l in lam]
print(avg_errors)
plt.ylabel("avg_error")
plt.xlabel("regularizer")
plt.semilogx(lam,avg_errors)


# In[20]:


#Formatting np range for plotting polynomial
deg =8
P_train = degexpand(X_train,deg)
P_test =  degexpand(X_test,deg)
W_ml = poly_ridge_regression(1,P_train,t_train)
ev = np.arange(min(X_3), max(X_3) + 0.1, 0.1)
x_ev = np.ones((ev.shape[0],1))
x_ev[:,0] = ev
x_ev_expanded = degexpand(x_ev,deg)

fig, axs = plt.subplots(len(lam))
fig.set_figwidth(15)
fig.set_figheight(20)
fig.suptitle("Effect of regularizer value on polynomial curve")
plt.xlim([-2,4])
plt.ylim([-2,5])
for i in range(0,len(lam)):
    W_ml = poly_ridge_regression(lam[i],P_test,t_test)
    poly_x = learned_polynomial(x_ev_expanded, W_ml)
    axs[i].set_title("lambda : {}".format(lam[i]))
    axs[i].plot(X_train, t_train, 'b.', ms = 1,markerfacecolor = 'none', label = "Training data")
    axs[i].plot(X_test,t_test, 'r.', ms =1,markerfacecolor = 'none', label = "Testing data")
    axs[i].plot(x_ev, poly_x, 'g-')

plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.9,
                    hspace=0.4)

plt.show()


# In[21]:


fig, axs = plt.subplots(1)
fig.set_figwidth(10)
fig.set_figheight(5)
fig.suptitle("Plot of the optimal curve, Lambda = {}".format(1000))
plt.xlim([-2,4])
plt.ylim([-2,5])
#Plot data
W_ml = poly_ridge_regression(1000,P_test,t_test)
poly_x = learned_polynomial(x_ev_expanded, W_ml)
axs.plot(X_train, t_train, 'b.', ms = 2,markerfacecolor = 'none', label = "Training data")
axs.plot(X_test,t_test, 'r.', ms =2,markerfacecolor = 'none', label = "Testing data")
axs.plot(x_ev, poly_x, 'g.-', ms = 10, label = "Polynomial")

axs.legend()
plt.show

