# ref: https://www.geeksforgeeks.org/python-count-occurrences-of-each-word-in-given-text-file-using-dictionary/

import numpy as np

# Open pattern file in read mode
with open('translatedFS-6orlonger.txt', 'r') as f:
    patterns = f.readlines()
f.close()

# Create an empty dictionary
d = dict()

# List representation of patterns that will be imported in example.py
data = []

# Loop through each pattern of the file
for line in patterns:
    # Split pattern sequence from support count
    pattern = line.split(" 	")[0]
    
    # Split pattern into individual events
    events = pattern.split(" ")

    # Temp list for line
    temp = []

    # Iterate over each event in pattern
    for event in events:
        # Check if the event is already in dict
        if event in d:
            # Increment count of event by 1
            d[event] = d[event] + 1
        else:
            # Add the event to dict with count 1
            d[event] = 1
        # Append event to temp list
        #temp.append(event)
    
    # Append pattern to data list
    #data.append([pattern, pattern])
    data.append(pattern)

# Test: Print the contents of dict
for key in list(d.keys()):
    print(key, ":", d[key])

# print(data)