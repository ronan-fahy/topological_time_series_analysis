#!/usr/bin/python3

import math, csv, collections

# Read CSV file into 1-dimensional time-series
#
# filepath: path to CSV file to be read from
# n:        number of rows to read
# Y:        returned time-series
def csv_to_time_series(filepath, n):
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile)
        Y = {}
        for row in reader:
            t, y = row
            if t and y:
                Y[int(t)] = float(y)
    Y = collections.OrderedDict(sorted(Y.items()))
    Y = {k: Y[k] for k in list(Y)[:n]}
    return Y

# Filter based on threshold
#
# h:        return only entries with value greater than h
# Y:        time-series to be filtered
def threshold(h, Y):
    return {t : Y[t] for t in Y if Y[t] > h}

# Create clusters
#
# times:    
# epsilon: 
# clusters:
def create_clusters(times, epsilon):
    clusters = [[]]
    prev_t = list(times)[0]
    cluster_idx = 0
    clusters[cluster_idx] = []
    for t in times:
        if (abs(t - prev_t)) < epsilon:
            clusters[cluster_idx].append(t)
        else:
            cluster_idx += 1
            clusters.append([t])
        prev_t = t
    return clusters

# Calculate averages
#
# clusters: 
# averages:
def calculate_averages(clusters):
    averages = []
    for cluster in clusters:
        total = 0
        for t in cluster:
            total += t
        averages.append(total/len(cluster))
    return averages

# Calculate differences
#
# averages:
# differences: 
def calculate_differences(averages):
    differences = []
    prev_average = averages[0]
    for average in averages[1:]:
        differences.append(average - prev_average)
        prev_average = average
    return differences

# ****************************************************
# Create takens embedding
#
# S:    time-series in dictionary form with time as
#       key
# d:    dimension of Takens embedding
# tau:  delay, how far back in the time-series to look
# T:    Takens embedding in form of dictionary with
#       mean time as key and vector as value
# ****************************************************
def Takens(S, d, tau):
    T = {}
    for i, (t, value) in enumerate(S.items()):
        if i%tau == 0 and i != 0:
            mean_time = 0
            temp = []
            for j in range(0, d):
                try:
                    #idx = int(round(t-((j*tau)/d)))
                    #temp = [S.get(idx)] + temp
                    idx = t-((j*tau)/d)
                    temp = [S[idx] if idx in S else S[min(S.keys(), key = lambda k: abs(k-idx))]] + temp
                    mean_time = mean_time + idx
                except TypeError:
                    print("d and tau must be integers greater than one")
            mean_time = mean_time / d
            T[mean_time] = temp

    return T

# ****************************************************
# Compute Euclidean distance between v and w
#
# v: vector
# w: vector
# m: calculated distance between v and w
# ****************************************************
def EuclideanMetric(v, w):
    if len(v) != len(w):
        raise ValueError('v and w must have equal length')
    m = 0
    for a, b in zip(v, w):
        m = m + (a - b) ** 2
    return math.sqrt(m)

# ****************************************************
# Compute taxicab distance between v and w
#
# v: vector
# w: vector
# m: calculated distance between v and w
# ****************************************************
def TaxicabMetric(v, w):
    if len(v) != len(w):
        raise ValueError('v and w must have equal length')
    m = 0
    for a, b in zip(v, w):
        m = m + abs(a - b)
    return m

# ****************************************************
# Get neighbourhood of v in T
# 
# T:       Takens embedding in form of dictionary with
#          mean time as key and vector as value
# v:       vector from T
# d:       dimension of Takens embedding
# epsilon: nearness threshold
# x:       subsequence of T in the neighbourhood of v
# ****************************************************
def Neighbourhood(T, v, d, epsilon):
    x = {}
    for t, w in T.items():
        if EuclideanMetric(v, w) < epsilon:
            x[t] = w
    return x

def t(Y):
    return Y.keys()

def m(Y):
    return Y.values()
