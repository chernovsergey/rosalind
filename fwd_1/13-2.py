import sys
import itertools

def repeat(s, pattern):
	count = 0
	l = len(s)
	k = len(pattern)
	for i in range(l - k + 1):
		if pattern == s[i:i+k]:
			count = count + 1
	return count

def pr(n, a, pattern, t):
	nmers = list(itertools.product(a, repeat = n))
	count = 0
	for i in nmers:
		s = ''
		for j in range(n):
			s = s + i[j]
		r = repeat(s, pattern)
		if r >= t:
			count = count + 1
	return float(count)/float(len(nmers))

print pr(7, '012', '11', 2)