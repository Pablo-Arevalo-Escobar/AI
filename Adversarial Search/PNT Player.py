#!/usr/bin/env python
# coding: utf-8

# In[204]:


# Takes PNT input and returns the data as variables for direct access
def inputPNT():
    node = input("Please enter the desired input:")
    global nodesEvaluated  
    global nodesVisited 
    global maxDepth
    nodesEvaluated = 0
    nodesVisited = 0
    maxDepth = 0

    #Removing spaces
    node = node[::2]
    if(node[1]%2 == 0):
        isMax = True
    else:
        isMax = False
        
    if node[len(node)-1]!= 0:
        depthLimit = node[len(node)-1]+1
    else:
        depthLimit = 0
        
    alphabeta(node, depthLimit, -math.inf, math.inf, isMax,0)

def directPNT(node):
    global nodesEvaluated  
    global nodesVisited 
    global maxDepth
    nodesEvaluated = 0
    nodesVisited = 0
    maxDepth = 0
    
    if(node[1]%2 == 0):
        isMax = True
    else:
        isMax = False
        
    if node[len(node)-1]!= 0:
        depthLimit = node[len(node)-1]+1
    else:
        depthLimit = 0
        
    alphabeta(node, depthLimit, -math.inf, math.inf, isMax,0)
    


# In[ ]:





# In[3]:


# GUIDE TO GETTING INFORMAITON FROM THE NODE LIST
#     numOfTokens = node[0]
#     numOfTaken = node[1]
#     listOfTaken = node[2:len(node)-1]
#.    lastMove = node[len(node)-2]
#     depth = node[len(node)-1]


# In[205]:


#Defining math helper functions for the heuristic e(n)
import math 

# If n is a composite integer, then n has a prime divisor less than
# or equal to √n
def isPrime(n):
    if(n < 2):
        return False
    else:
        for i in range(2,math.floor(math.sqrt(n))+1):
            if isPrime(i):
                if n%i == 0:
                    return False
        return True


def largePrimeFactor(n):
    largePrime = -1 
    for i in range(2,n):
        if isPrime(i):
            if n%i == 0:
                largePrime = i    
    return largePrime


# In[206]:


#Defining node helper functions for heuristic e(n)
# def succesorCount(node):
    
def succesorCount(node):
    return countMultiples(node,-1)+countFactors(node)
    
def countMultiples(node, prime):
    numOfTokens = node[0]
    listOfTaken = node[2:len(node)-1]
    
    #Forming a set to improve search time for large lists
    s = set(listOfTaken)
    count = 0
    
    if(prime == -1):
        parent = node[len(node)-2]
    else:
        parent = prime
        if(prime not in s):
            count+=1

    #Checking that there are multiples
    if numOfTokens < parent*2:
        return count;

    #numOfTokens/parent tells us how many multiples of the parent
    #there are in the set of successors 
    for i in range(2, int(numOfTokens/parent)+1):
        if parent*i not in s:
            count += 1
    return count

def countFactors(node):
    numOfTokens = node[0]
    parent = node[len(node)-2]
    listOfTaken = node[2:len(node)-1]
    s = set(listOfTaken)
    
    if parent < 4:
        if 1 in s:
            return 0
        else:
            return 1
        
    count = 0 
    for i in range(1, parent):
        if parent%i == 0:
            if i not in s:
                count +=1 
    return count

#Defining alpha-beta and e(n) shared helper-function
def gameOver(node):
    if(node[1] == 0):
        return False
    if succesorCount(node) == 0:
        return True
    else:
        return False


# In[207]:


# Defining heuristic function e(n)/ static board evaluation
# Assume MAX always plays first (thus all even turns are MAX's)
def e(node):
    numOfTokens = node[0]
    numOfTaken = node[1]
    lastMove = node[len(node)-2]
    
    #Checking if it's the first move
    if numOfTaken == 0:
        return 0;
    
    #Checking endGame state
    if gameOver(node):
        return -1 if numOfTaken%2 == 0 else 1
    
    if lastMove == 1:
        count = succesorCount(node)
        if numOfTaken%2 == 0:
            return 0.5 if count%2 != 0 else -0.5 
        #MIN Turn
        else:
            return -0.5 if count%2 != 0 else 0.5 
        
        
    if isPrime(lastMove):
        #Count multiples of prime in possible succesors
        count = countMultiples(node,-1)
        #Max Turn
        if numOfTaken%2 == 0:
            return 0.7 if count%2 != 0 else -0.7 
        #MIN Turn
        else:
            return -0.7 if count%2 != 0 else 0.7

    else:
        #Find largest prime that can divide lastMove
        prime = largePrimeFactor(lastMove)
        #Count multiples of said prime (including prime itself)
        count = countMultiples(node,prime)
        #Max Turn
        if numOfTaken%2 == 0:
            return 0.6 if count%2 != 0 else -0.6 
        #MIN Turn
        else:
            return -0.6 if count%2 != 0 else 0.6    


# In[208]:


#Defining node related functions
def children(node):
    children = []
    numOfTokens = node[0]
    numOfTaken = node[1]
    
    if node[1]!=0:
        listOfTaken = node[2:len(node)-1]
        parent = listOfTaken[len(listOfTaken)-1]
        s = set(listOfTaken)
    else:
        #FIRST TURN LOGIC - ODD NUMBERS LESS THAN N/2
        for i in range(1,math.ceil(numOfTokens/2)):
            if i%2 != 0:
                children.append([node[0],node[1]+1,i,node[len(node)-1]])
        return children
    
    
    #numOfTokens/parent tells us how many multiples of the parent
    #there are in the set of successors 
    for i in range(2, int(numOfTokens/parent) + 1):
        if parent*i not in s:
            child = [node[0],node[1]+1]
            for value in listOfTaken:
                child.append(int(value))
            child.append(parent*i)
            child.append(node[len(node)-1])
            children.append(child)
   
    #Factor children
    if parent < 4:
        if 1 not in s:
            child = [node[0],node[1]+1]
            #listOfTaken
            for value in listOfTaken:
                child.append(int(value))
            child.append(1)
            child.append(node[len(node)-1])
            children.append(child)
    else:
        for i in range(1,parent):
            if parent%i == 0:
                if i not in s:
                    child = [node[0],node[1]+1]
                    for value in listOfTaken:
                        child.append(int(value))
                    child.append(i)
                    child.append(node[len(node)-1])
                    children.append(child)
                    
    return children


# In[209]:


# Function template for alphabeta pruning 
def alphabeta(node, depthLimit, alpha, beta,isMax, depth):
    global nodesEvaluated
    global nodesVisited
    global maxDepth
    maxDepth = max(maxDepth, depth)
    nodesVisited += 1
    
    if gameOver(node) or depthLimit == 1:
        nodesEvaluated +=1
        return e(node)
    

    if isMax:
        v = -math.inf
        childList = children(node)
        for child in children(node):
            newV = alphabeta(child, depthLimit-1, alpha, beta, False,depth+1)
            if newV > v and depth == 0:
                move = child[len(child)-2]
            v = max(v,newV )
            alpha = max(alpha, v)
            if(beta <= alpha):
                break
                
        if depth == 0:
            avgEffectiveBranching = (nodesVisited-1)/(nodesVisited-nodesEvaluated)
            avgEffectiveBranching = round(avgEffectiveBranching,1)
            print("Move: " + str(move))
            print("Value: " + str(v))
            print("Number of Nodes Visited: " + str(nodesVisited))
            print("Number of Nodes Evaluated: " + str(nodesEvaluated))
            print("Max Depth Reached: " + str(maxDepth))
            print("Avg Effective Branching Factor: " + str(avgEffectiveBranching))
        else:
            return v
    
    else:
        v = math.inf
        childList = children(node)
        for child in children(node):
            newV= alphabeta(child, depthLimit-1, alpha, beta, True,depth+1)
            if newV < v and depth == 0:
                move = child[len(child)-2]
            v = min(v, newV)
            beta = min(beta, v)
            if beta <= alpha:
                break
        if depth == 0:
            avgEffectiveBranching = (nodesVisited-1)/(nodesVisited-nodesEvaluated)
            avgEffectiveBranching = round(avgEffectiveBranching,1)
            print("Move: " + str(move))
            print("Value: " + str(v))
            print("Number of Nodes Visited: " + str(nodesVisited))
            print("Number of Nodes Evaluated: " + str(nodesEvaluated))
            print("Max Depth Reached: " + str(maxDepth))
            print("Avg Effective Branching Factor: " + str(avgEffectiveBranching))

        else:
            return v
                
    


# In[210]:


# directPNT([3,0,0])
# directPNT([7,1,1,2])
# directPNT([10, 3, 4, 2, 6 ,4])
# directPNT([8,3,3,1,2,0])
# directPNT([10,5,3,1,8,4,2,0])


# In[ ]:


import sys
if __name__ == "__main__":
    node = [int(i) for i in sys.argv[1::]]
    directPNT(node)

