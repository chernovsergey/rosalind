import sys

n = 6
k = 20
cur = [0 for i in range(n)]

def gen(pos):
	if pos == n:
		for i in range(n):
			sys.stdout.write(str(cur[i]))
		print ''
		return
	for i in range(k):
		cur[pos] = i
		gen(pos + 1)

gen(0)