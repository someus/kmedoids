# kmedoids
The Python implementation of [k-medoids](https://en.wikipedia.org/wiki/K-medoids). 

## Example
```python
from sklearn.metrics.pairwise import pairwise_distances
import numpy as np

import kmedoids

# 3 points in dataset
data = np.array([[1,1], 
                [2,2], 
                [10,10]])

# distance matrix
D = pairwise_distances(data, metric='euclidean')

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
```

Output:
```
medoids:
[1 1]
[10 10]

clustering result:
label 0:　[1 1]
label 0:　[2 2]
label 1:　[10 10]
```

## License
This code is from:

> Bauckhage C. Numpy/scipy Recipes for Data Science: k-Medoids Clustering[R]. Technical Report, University of Bonn, 2015.

Please cite the article if the code is used in your research.