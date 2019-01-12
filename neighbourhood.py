#!/usr/bin/python3

# ***************************************************
# T:       time-series in form of list of lists
# v:       vector from T, list
# d:       dimension of embedding
# epsilon: nearness threshold
# x:       subsequence of T in the neighbourhood of v
# ***************************************************
from euclidean_metric import EuclideanMetric

def Neighbourhood(T, v, d, epsilon):
    for y in T:
        if EuclideanMetric(y, v) < epsilon:
            x.append(y)
    return x
