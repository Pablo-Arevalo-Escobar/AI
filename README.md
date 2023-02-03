# AI
A collection of python code exploring a variety of AI methods

## Contents 

- [Neural Net](#neural-net)

- [Clustering](#clustering)

- [Sentiment Analysis](#sentiment-analysis)


## Neural Net
A neural net implemented through Python to solve the XOR problem.

Classifiers such as uni layered perceptrons can only handle linearly separable data, making them unable to solve non-linear problems like the XOR problem. Neural nets (or Multi Layered Perceptrons), however, are capable of handling such non-linear problems, making the XOR problem a suitable demonstration of their applications.


### XOR Illustration

![](Images/XOR.png)


### Classifier Decision Boundary

![](Images/DecisionBoundary.png)


### Final and Hidden Output Functions

![](Images/OutputFunctions.png)





### References
  [1] https://medium.com/analytics-vidhya/coding-a-neural-network-for-xor-logic-classifier-from-scratch-b90543648e8a
  
  [2] https://towardsdatascience.com/how-neural-networks-solve-the-xor-problem-59763136bdd7
  
  [3] https://dev.to/jbahire/demystifying-the-xor-problem-1blk

## Clustering 

K-Means clustering implementation performed on a sample image of Obama.


### Data Formatting

![](Images/ClusteringDataFormatting.png)
![](Images/ObamaOriginal.png)



### Results

![](Images/ClusteringResults.png)
![](Images/ObamaClustered.png)



## Sentiment Analysis

A Python program that takes in a set of sentiment labeled reviews.

A Naive-Bayes classifier and Decision-Tree classifer are trained and tested using an 80-20 split on the provided data.

### Data Sentiment Spread

![](Images/CountOfSentimentType.png)


### Naive Bayes : Testing Results

| Smoothing |    Accuracy   | Weighted Recall |  Weighted Precision | Weighted F1-Measure |
|-----------| ------------- | -------------   | --------------------| --------------------|
|   0.05    | 0.819135543432|  0.819135543432 |    0.819237343523   |    0.819162061498   |

Naive-Bayes (smoothing = 0.05) accuracy :  0.8191355434326479

Naive-Bayes (smoothing = 0.05) weighted recall :  0.8191355434326479

Naive-Bayes (smoothing = 0.05) weighted precision :  0.8192373435226762

Naive-Bayes (smoothing = 0.05) weighted f1-measure :  0.8191620614979724

### Base Decision Tree : Testing Results

Base-DT accuracy :  0.6852706672261855

Base-DT weighted recall :  0.6852706672261855

Base-DT weighted precision :  0.6865627421261534

Base-DT weighted f1-measure :  0.6852906195529649

### Best Decision Tree : Testing Results

Best-DT accuracy :  0.7184221569450273

Best-DT weighted recall :  0.7184221569450273

Best-DT weighted precision :  0.7186792192777415

Best-DT weighted f1-measure :  0.7184837731655974
