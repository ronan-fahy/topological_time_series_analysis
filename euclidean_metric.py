#!/usr/bin/python3

import math

def EuclideanMetric(v, w):
    sum = 0
    for a, b in zip(v, w):
        sum += (a - b) ** 2

    return math.sqrt(sum)
