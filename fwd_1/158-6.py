import sys
import itertools

def mismatch(s1, s2):
	size = len(s1)
	count = 0
	for i in range(size):
		if s1[i] != s2[i]:
			count = count + 1
	return count

def minMismatch(s, ss, k):
	l = len(s)
	bestDist = sys.maxint
	for i in range(l-k+1):
		d = mismatch(ss, s[i:i+k])
		if d <= bestDist:
			bestDist = d
	return bestDist

k = 6

f = open("input.txt", "r")
dna = f.read().split('\n')

patterns = list(itertools.product("TGAC", repeat=k))

bestPattern = ''
bestD = sys.maxint

for i in patterns:
	p = ''
	for t in i:
		p = p + t
	count = 0	
	for j in dna:
		count = count + minMismatch(j, p, k)
	if count < bestD:
		bestPattern = p
		bestD = count

print bestPattern