import sys
import itertools

def mismatch(s1, s2):
	size = len(s1)
	count = 0
	for i in range(size):
		if s1[i] != s2[i]:
			count = count + 1
	return count

def count(text, pattern, d):
	l = len(text)
	k = len(pattern)
	count = 0
	for i in range(l - k + 1):
		if mismatch(pattern, text[i:i+k]) <= d:
			count = count + 1
	return count

s = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 1

out = []
value = -1

patterns = list(itertools.combinations_with_replacement('ACGT', k))

for i in patterns:
	ptr = ''
	for j in range(k):
		ptr = ptr + i[j]
	c = count(s, ptr, d)
	if c > value:
		out = []
		out.append(ptr)
		value = c
	elif c == value:
		out.append(ptr)

print value
for i in out:
	print i,