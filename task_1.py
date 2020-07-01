#!/usr/bin/python3

from topological_time_series_analysis import *
import collections, sys
import matplotlib.pyplot as plt

filePath = sys.argv[1]
n        = 5000
h        = 4
epsilon  = 4

# Read in CSV file
Y = csv_to_time_series(filePath, n)

# Threshold
Y = threshold(h, Y)
clusters = create_clusters(t(Y), epsilon)
averages = calculate_averages(clusters)
differences = calculate_differences(averages)

plt.plot(list(t(Y)),list(m(Y)),'ro')
plt.show()
