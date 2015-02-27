import sys
from collections import defaultdict

k = 3
t = 5

dna = open("input.txt", "r").read().split("\n")

profile = defaultdict(list)

kmers = defaultdict(int)

for i in dna:
	l = len(i)
	for j in range(l-k):
		kmers[i[j:j+k]] = kmers[i[j:j+k]] + 1
print kmers