import importpattern

# longest common subsequence - length
# ref: https://stackoverflow.com/questions/24547641/python-length-of-longest-common-subsequence-of-lists
# param: two lists
def lcs_length(a, b):
    table = [[0] * (len(b) + 1) for _ in xrange(len(a) + 1)]
    for i, ca in enumerate(a, 1):
        for j, cb in enumerate(b, 1):
            table[i][j] = (
                table[i - 1][j - 1] + 1 if ca == cb else
                max(table[i][j - 1], table[i - 1][j]))
    return table[-1][-1]

# occurrence frequency of each event
def occ(a, b, union):
    docc = 0
    ftotal = 0
    
    # a and b
    intersect = [value for value in a if value in b]

    if len(intersect) == 0:
        return 1
    else:
        # calculate Ftotal
        for u in union:
            #print(u)
            ftotal = ftotal + importpattern.d[u]
            #print(ftotal)
        
        # calculate Docc
        for event in intersect:
            #print(importpattern.d[event])
            docc = docc + (float(importpattern.d[event])/ftotal)
            print(docc, float(importpattern.d[event])/ftotal)
        
        #print(docc)
        return docc