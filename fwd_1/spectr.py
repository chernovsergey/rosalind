import sys

table = {'':0, 'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'I':113, 'L':113, 'N':114, 'D':115, 'K':128, 'Q':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186}

def mass(s):
	m = 0
	for i in s:
		m = m + table[i]
	return m

ss = ['PVCPT']

for s in ss:
	out = []
	out.append(0)

	k = len(s)
	for i in range(1, k):
		for j in range(k):
			if j+i<=k:
				out.append(mass(s[j:j+i]))
			else:
				out.append(mass(s[j:k]+s[0:j+i-k]))
	out.append(mass(s))
#	out.sort()
	print s,
	for i in out:
		print i,	
	print ''