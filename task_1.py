#!/usr/bin/python3

from topological_time_series_analysis import *
import collections
import matplotlib as plt

filePath = "sea_level_data_complete.csv"
n        = 5000
h        = 4
epsilon  = 4

# Read in CSV file
Y = csv_to_time_series(filePath, n)

# Threshold
Y = threshold(h, Y)

times = t(Y)
#times = [t * 6 for t in times]

clusters = create_clusters(times, epsilon)

averages = calculate_averages(clusters)
print(averages)

differences = calculate_differences(averages)
