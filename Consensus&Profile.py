__author__ = 'Sergey'

import numpy as np


def extractData(fname):
    Names, Strands = [], []
    summary_strand = str("")
    f = open(fname, 'r')
    for line in f.read().split('\n'):
        if line.startswith('>'):
            Names.append(line.replace('>', ''))
            summary_strand += "-"
        else:
            summary_strand += line
    f.close()
    Strands = summary_strand.split("-")
    Strands = [x for x in Strands if len(x) != 0]
    return Names, Strands


names, strands = extractData("Consensus&Profile.txt")

len_of_str = len(strands[0])
mat = np.matrix(np.zeros((4, len_of_str), dtype=int))
columns = []
for j in range(len_of_str):
    s = ""
    for i in strands:
        a = i[j]
        s += a
    columns.append(s)
for i in range(len(columns)):
    a = str(columns[i]).count('A')
    c = str(columns[i]).count('C')
    g = str(columns[i]).count('G')
    t = str(columns[i]).count('T')
    mat[0, i] = a
    mat[1, i] = c
    mat[2, i] = g
    mat[3, i] = t

consensus = ""
for i in mat.T:
    m = max(np.ravel(i))
    col = (np.ravel(i)).tolist()
    for j in range(len(col)):
        if col[j] == m:
            if j == 0:
                consensus += 'A'
            if j == 1:
                consensus += 'C'
            if j == 2:
                consensus += 'G'
            if j == 3:
                consensus += 'T'

print consensus,
print

print "A:",
for i in np.ravel(mat[0]):
    print i,
print

print "C:",
for i in np.ravel(mat[1]):
    print i,
print
print "G:",
for i in np.ravel(mat[2]):
    print i,
print
print "T:",
for i in np.ravel(mat[3]):
    print i,
