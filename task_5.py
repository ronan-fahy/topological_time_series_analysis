#!/usr/bin/python3

from topological_time_series_analysis import *
import sys
import matplotlib.pyplot as plt

filepath = sys.argv[1]
n = 5000
d = 50
tau = 20
epsilon = 1000

Y = csv_to_time_series(filepath, n)
S = m(Y)
T = Takens(Y, d, tau)
w0 = next(iter(T.values()))
N = Neighbourhood(T, w0, d, epsilon)
tN = t(N)
clusters = create_clusters(tN, epsilon)
averages = calculate_averages(clusters)
differences = calculate_differences(averages)

n, bins, patches = plt.hist(differences)
plt.show()
