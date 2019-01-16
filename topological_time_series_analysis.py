#!/usr/bin/python3

import math

# ****************************************************
# Create takens embedding
#
# S:    time-series in dictionary form
# d:    dimension of embedding
# tau:  delay, how far back in the time-series to look
# T:    Takens embedding in form of dictionary
# ****************************************************
def Takens(S, d, tau):
    T = {}
    for i, (t, value) in enumerate(S.items()):
        if (i+1)%tau == 0:
            mean_time = 0
            temp = []
            for j in range(0, d):
                mean_time = mean_time + t
                try:
                    temp = [S.get(int(max(0, round(t-((j*tau)/d)))))] + temp
                except TypeError:
                    print("d and tau must be integers greater than one")
            mean_time = mean_time / d
            T[mean_time] = temp
            
    return T

# ****************************************************
# Compute distance between v and w
#
# v: point in embedding
# w: point in embedding
# ****************************************************
def EuclideanMetric(v, w):
    sum = 0
    for a, b in zip(v, w):
        sum += (a - b) ** 2

    return math.sqrt(sum)

# ****************************************************
# Get neighbourhood of v in T
# 
# T:       Takens embedding in form of dictionary
# v:       vector from T, list
# d:       dimension of embedding
# epsilon: nearness threshold
# x:       subsequence of T in the neighbourhood of v
# ****************************************************
def Neighbourhood(T, v, d, epsilon):
    x = {}
    for t, w in T.items():
        if EuclideanMetric(v, w) < epsilon:
            x[t] = w
    return x

# ****************************************************
# Get some notion of time for each point in emedding
#
# w: point for which time must be gotten
# ****************************************************
#def t(w):
    
