# coding: utf-8
from sklearn.metrics.pairwise import pairwise_distances
from scipy.spatial.distance import pdist, squareform
import numpy as np

import kmedoids
import importpattern
import distmeasure

# Patterns in dataset
data = np.array(np.column_stack((importpattern.data, importpattern.data)))

# Alpha value to weigh ratios between two distance measures
alpha = .25

# Define custom dist function
def dfun(u, v):
    utemp = u[0].split(" ")
    vtemp = v[0].split(" ")

    usplit = []
    vsplit = []

    for eventu in utemp:
        usplit.append(eventu)
    for eventv in vtemp:
        vsplit.append(eventv)
    
    # u union v
    union = list(set(usplit) | set(vsplit))
    #print(union)

    # Dist measure 1 based on Longest Common Subsequence
    dlcs = 1-(abs(distmeasure.lcs_length(usplit, vsplit))/abs(len(union)))

    # Dist measure 2 based on the occurrence frequency of each event
    docc = distmeasure.occ(usplit, vsplit, union)

    return (alpha * dlcs) + ((1-alpha) * docc)


# distance matrix
D = squareform(pdist(data, lambda u, v: dfun(u, v)))

# split into 2 clusters
M, C = kmedoids.kMedoids(D, 2)

print('medoids:')
for point_idx in M:
    print( data[point_idx] )

print('')
print('clustering result:')
for label in C:
    for point_idx in C[label]:
        print('label {0}:　{1}'.format(label, data[point_idx]))


