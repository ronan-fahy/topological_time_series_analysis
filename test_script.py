#!/usr/bin/python3

from topological_time_series_analysis import *
import collections

filePath = "sea_level_data_complete.csv"
n        = 5000
d        = 50
tau      = 20
epsilon  = 4

# Read in CSV file
Y = csv_to_time_series(filePath, n)

# Form the Takens embedding
T = Takens(Y, d, tau)
ordered_T = collections.OrderedDict(sorted(T.items()))

# Get neighbourhood of some w in T
w0 = list(ordered_T.values())[0]
N = Neighbourhood(ordered_T, w0, d, epsilon)

# Get set of average times for each vector in N
times = t(N)
#times = [t * 6 for t in times]

# Cluster t_N
clusters = create_clusters(times, epsilon)

# Compute average time for each cluster
averages = calculate_averages(clusters)
print(averages)

# Compute differences
differences = calculate_differences(averages)
