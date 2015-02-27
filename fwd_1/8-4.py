import sys
import itertools

def reverse(s):
	d = {'A':'T', 'G':'C', 'T':'A', 'C':'G'}
	s = s[::-1]
	out = ''
	for i in s:
		out = out + d[i]
	return out

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

s = 'ATAAATCACGTCACGATATCACGAACGCGATAATAATATCAAAATATCATCATCATCATCACGTTTTCATCACGCGTCAAAAAATACGATAAACGTTTATAAATCACGTTTATACGATACGCGATAATATTTATACGTCATTTTTTATATTTCGATAATATTTATAATATTTTTTAACGATATCAAAATAATATTTAAAAATACGAATCATTTCGAAAAATATTTAATTTAAATACGTTT'
k = 8
d = 3

out = set()
value = -1

patterns = list(itertools.product('ACGT', repeat = k))

for i in patterns:
	ptr = ''
	for j in range(k):
		ptr = ptr + i[j]
	rptr = reverse(ptr)
	c1 = count(s, ptr, d)
	c2 = count(s, rptr, d)
	c = c1 + c2
	if c > value:
		out = set()
		out.add(ptr)
		out.add(rptr)
		value = c
	elif c == value:
		out.add(ptr)
		out.add(rptr)

for i in out:
	print i,