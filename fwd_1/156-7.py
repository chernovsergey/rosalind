import sys
import itertools

def mismatch(s1, s2):
	size = len(s1)
	count = 0
	for i in range(size):
		if s1[i] != s2[i]:
			count = count + 1
	return count

def maxRepeat(s, ss, d, k):
	l = len(s)
	for i in range(l-k+1):
		if mismatch(ss, s[i:i+k]) <= d:
			return 1
	return 0

k = 5
d = 1

f = open("input.txt", "r")
dna = f.read().split('\n')

patterns = list(itertools.product("TGAC", repeat=k))

for i in patterns:
	flag = 1
	for j in dna:
		if maxRepeat(j, i, d, k) == 0:
			flag = 0
			break
	if flag == 1:
		for t in range(k):
			sys.stdout.write(i[t])
		sys.stdout.write(' ')