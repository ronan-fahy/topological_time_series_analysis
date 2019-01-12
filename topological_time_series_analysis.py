#!/usr/bin/python3

from euclidean_metric import EuclideanMetric
import math

# ****************************************************
# Create takens embedding
#
# S:    time-series in dictionary form
# d:    dimension of embedding
# tau:  delay, how far back in the time-series to look
# T:    time-series in form of list of lists
# ****************************************************
def Takens(S, d, tau):
   
    if d < 1:
        print("d must be greater than or equal to 1")
        return

    if tau < 1:
        print("tau must be greater than or equal to 1")
        return

    T = []
    for i, (t, value) in enumerate(S.items()):
        if (i+1)%tau == 0:
            temp = []
            for j in range(0, d):
                try:
                    temp = [S.get(t-((j*tau)/d))] + temp
                except TypeError:
                    print("d and tau must be integers greater than one")
            T.append(temp)
            
    return T

# ********************************
# Compute distance between v and w
#
# v: 
# w: 
# ********************************
def EuclideanMetric(v, w):
    sum = 0
    for a, b in zip(v, w):
        sum += (a - b) ** 2

    return math.sqrt(sum)

# ***************************************************
# Get neighbourhood of v in T
# 
# T:       time-series in form of list of lists
# v:       vector from T, list
# d:       dimension of embedding
# epsilon: nearness threshold
# x:       subsequence of T in the neighbourhood of v
# ***************************************************
def Neighbourhood(T, v, d, epsilon):
    for y in T:
        if EuclideanMetric(y, v) < epsilon:
            x.append(y)
    return x
