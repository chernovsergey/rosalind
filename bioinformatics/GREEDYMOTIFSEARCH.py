import re

def Score(motifList):
    k = len(motifList[0])
    d = dict()
    d['A'] = 0
    d['C'] = 1
    d['G'] = 2
    d['T'] = 3

    profile = []
    for i in range(k):
        profile.append([0])
        for j in range(3):
            profile[i].append(0)

    for i in range(k):
        for j in motifList:
            profile[i][d[j[i]]] += 1
    return sum([max(i) for i in profile])


def Profile(motifList):
    k = len(motifList[0])
    d = dict()
    d['A'] = 0
    d['C'] = 1
    d['G'] = 2
    d['T'] = 3

    profile = []
    for i in range(k):
        profile.append([1])
        for j in range(3):
            profile[i].append(1)

    for i in range(k):
        for j in motifList:
            profile[i][d[j[i]]] += 1
    for i in range(k):
        for j in range(4):
            profile[i][j] /= len(motifList) + 4
    return profile


def probability(pattern, profile):
    d = dict()
    d['A'] = 0
    d['C'] = 1
    d['G'] = 2
    d['T'] = 3
    tmp = 1
    for i in range(k): tmp *= profile[i][d[pattern[i]]]
    return tmp


def BestPattern(text, profile, k):
    max_probability = 0
    best_pattern = text[:k]
    for i in range(len(text) - k + 1):
        tmp = probability(text[i:i + k], profile)
        if tmp > max_probability:
            max_probability = tmp
            best_pattern = text[i:i + k]
    return best_pattern


def GREEDYMOTIFSEARCH(Dna, k, t):
    bestScore = 0
    bestMotifs = []
    for i in range(len(Dna[0]) - k + 1):
        curMotifs = []
        curMotifs.append(Dna[0][i:i + k])
        for j in range(1, t):
            motif = BestPattern(Dna[j], Profile(curMotifs), k)
            curMotifs.append(motif)
        if bestScore < Score(curMotifs):
            bestScore = Score(curMotifs)
            bestMotifs = curMotifs
    return bestMotifs


Dna = []
f = open("greedymotifsearch.txt", "r").readlines()
k, t = f[0].split(' ')
k = int(k)
t = int(t)
print k, t
for i in range(1, len(f)):
    Dna.append(re.sub('\n', '', f[i]))


for i in GREEDYMOTIFSEARCH(Dna, k, t):
    print(i)