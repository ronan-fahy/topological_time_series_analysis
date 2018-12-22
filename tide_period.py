#!/usr/bin/python3

import csv
import matplotlib.pyplot as plt

def threshold(h, Y):
    return {t : Y[t] for t in Y if Y[t] > h}

# Read in CSV file
with open('sea_level_data_complete.csv') as csvfile:
    reader = csv.reader(csvfile)
    Y = {}
    for row in reader:
        t, y = row
        Y[int(t)] = float(y)
Y = {k: Y[k] for k in list(Y)[:2000]}
plt.plot(list(Y.keys()), list(Y.values()))
plt.show()

# Filter based on threshold
h = 3.7
Y = threshold(h, Y)
#plt.plot(list(Y.keys()), list(Y.values()))
#plt.show()
times = Y.keys()

# Take first 1000 times
#times = list(times)[:100000]
times = list(times)

# Create clusters
epsilon = 100
clusters = [[]]
prev_t = times[0]
cluster_idx = 0
clusters[cluster_idx] = []
for t in times:
    if (abs(t - prev_t)) < epsilon:
        clusters[cluster_idx].append(t)
    else:
        cluster_idx += 1
        clusters.append([t])
    prev_t = t
#for cluster in clusters:
    #print(cluster)

# Calculate averages
averages = []
for cluster in clusters:
    total = 0
    for t in cluster:
        total += t
    averages.append(total/len(cluster))
#print(averages)

# Calculate differences
differences = []
prev_average = averages[0]
for average in averages[1:]:
    differences.append(average - prev_average)
    prev_average = average
#print(differences)

# Plot averages and differences
#averages_line, = plt.plot(averages, 'ro', label='peak times')
differences_line, = plt.plot(differences, 'bo', label='period')
plt.xlabel('index')
plt.ylabel('time (minutes)')
plt.legend(handles=[differences_line])
plt.show()

# Write period values to CSV file
#with open("period_data.csv", 'w') as results_file:
#    writer = csv.writer(results_file)
#    writer.writerow(differences)
