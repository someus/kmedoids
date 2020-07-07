# ref: https://www.geeksforgeeks.org/python-count-occurrences-of-each-word-in-given-text-file-using-dictionary/

# Open pattern file in read mode
with open('translatedFS-6orlonger.txt', 'r') as f:
    patterns = f.readlines()
f.close()

# Create an empty dictionary
d = dict()

# Loop through each pattern of the file
for line in patterns:
    # Split pattern sequence from support count
    pattern = line.split(" 	")[0]
    
    # Split pattern into individual events
    events = pattern.split(" ")

    # Iterate over each event in pattern
    for event in events:
        # Check if the event is already in dict
        if event in d:
            # Increment count of event by 1
            d[event] = d[event] + 1
        else:
            # Add the event to dict with count 1
            d[event] = 1

# Test: Print the contents of dict
for key in list(d.keys()):
    print(key, ":", d[key])