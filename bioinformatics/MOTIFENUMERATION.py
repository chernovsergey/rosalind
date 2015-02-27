import itertools

alphabet = "ACGT"
k = 5
d = 2

lines = ["GCTCATAGTCAATATTTCTGACCGC",
         "GAACGGCCAACCAACGCGCGTTCCG",
         "ATCGTTAAAAGTGAATATGGATCAG",
         "TGGAACGAGGGAAACATCCGGGAAT",
         "TTGTCGATTTATCGGCATTTTTGGA",
         "GCACTAAGTGTTCAGGTTGTGGGAA"]


def Dist(a, b):
    if len(a) != len(b): print("error in Dist function")
    tmp = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            tmp += 1
    return tmp


def DistInLine(a, line):
    if len(a) > len(line): print("error in DistInLine function")
    bestDist = len(a)
    for i in range(len(line) - len(a) + 1):
        if (Dist(a, line[i:i + len(a)]) < bestDist): bestDist = Dist(a, line[i:i + len(a)])
    return bestDist


allPatterns = [''.join(i) for i in itertools.product(alphabet, repeat=k)]

for i in allPatterns:
    maxDiff = 0
    for j in lines:
        if DistInLine(i, j) > maxDiff: maxDiff = DistInLine(i, j)
    if maxDiff <= d: print (i)

