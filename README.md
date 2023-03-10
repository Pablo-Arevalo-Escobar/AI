# AI
A collection of python code exploring a variety of AI methods

## Contents 

- [Neural Net](#neural-net)
    - [Decision Boundary](#classifier-decision-boundary)
    - [Output Functions](#final-and-hidden-output-functions) 

- [Clustering](#clustering)
    - [Data Formatting](#data-formatting)
    - [Results](#results)

- [Sentiment Analysis](#sentiment-analysis)
    - [Naive Bayes](#naive-bayes)
    - [Decision Tree](#decision-tree)
    
- [Regression](#regression)


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



## Sentiment Analysis[hw1.pdf](https://github.com/Pablo-Arevalo-Escobar/AI/files/10775564/hw1.pdf)


A Python program that takes in a set of sentiment labeled reviews.

A Naive-Bayes classifier and Decision-Tree classifer are trained and tested using an 80-20 split on the provided data.

### Data Sentiment Spread

![](Images/CountOfSentimentType.png)

### Naive Bayes

#### Naive Bayes : Training Results

| Smoothing |    Accuracy   | Weighted Recall |  Weighted Precision | Weighted F1-Measure |
|-----------| ------------- | -------------   | --------------------| --------------------|
|   1.00    | 0.869793306053|  0.869793306053 |    0.870386391303   |     0.869789754171  |
|   0.25    | 0.871681880180|  0.871681880180 |    0.87218039395    |    0.871682335029   |
|   0.10    | 0.871891721750|  0.871891721750 |    0.872378943981   |    0.871892618677   |
|   0.05    | 0.871996642534|  0.871996642534 |    0.872478265022   |    0.871997755730   |
|   0.025   | 0.872311404889|  0.872311404889 |    0.872798854901   |    0.872312298878   |


#### Naive Bayes : Testing Results

| Smoothing |    Accuracy   | Weighted Recall |  Weighted Precision | Weighted F1-Measure |
|-----------| ------------- | -------------   | --------------------| --------------------|
|   0.05    | 0.819135543432|  0.819135543432 |    0.819237343523   |    0.819162061498   |




### Decision Tree

#### Decision Tree : Training Results


|    Accuracy   | Weighted Recall |  Weighted Precision | Weighted F1-Measure |
| ------------- | -------------   | --------------------| --------------------|
| 0.999895079215|  0.999895079215 |    0.999895101610   |    0.999895079402   |


#### Base Decision Tree : Testing Results


|    Accuracy   | Weighted Recall |  Weighted Precision | Weighted F1-Measure |
| ------------- | -------------   | --------------------| --------------------|
| 0.685270667226|  0.685270667226 |    0.686562742126   |    0.685290619552   |



#### Best Decision Tree : Testing Results


|    Accuracy   | Weighted Recall |  Weighted Precision | Weighted F1-Measure |
| ------------- | -------------   | --------------------| --------------------|
| 0.718422156945|  0.718422156945 |    0.718679219277   |    0.718483773165   |


## Regression
Linear and polynomial regression, theory and implementation, done as an assignment for Prof. Yang Wang at Concordia University Montreal, completed on the Winter 2023 semester.

[Report](https://github.com/Pablo-Arevalo-Escobar/AI/files/10775569/Report.pdf)


#### Polynomial Regression
![](Images/vis_spread.png)
![](Images/vis_M1png)
![](Images/vis_M6.png)
![](Images/vis_M15.png)

