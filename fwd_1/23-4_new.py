import sys

table = {'':0, 'G':57, 'A':71, 'S':87, 'P':97, 'V':99, 'T':101, 'C':103, 'L':113, 'N':114, 'D':115, 'K':128, 'E':129, 'M':131, 'H':137, 'F':147, 'R':156, 'Y':163, 'W':186}

def mass(s):
	m = 0
	for i in s:
		m = m + table[i]
	return m

def intersection(A, B):
	out = []
	k1 = len(A)
	k2 = len(B)
	for i in range(k1):
		for j in range(k2):
			if A[i] == B[j]:
				out.append(A[i])
				A[i] = -1
				B[j] = -1
				break
	out.sort()
	return out

def spectr(s):
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
	out.sort()
	sout = ''
	for i in out:
		sout = sout + str(i) + ' '
	return sout

def subspectr(s):
	out = []
	out.append(0)
	k = len(s)
	for i in range(1, k):
		for j in range(k):
			if j+i<=k:
				out.append(mass(s[j:j+i]))
	out.append(mass(s))
	out.sort()
	sout = ''
	for i in out:
		sout = sout + str(i) + ' '
	return sout


rtable = {}

for i in table.keys():
	rtable[table[i]] = i

s = '531 113 174 402 103 602 303 71 129 473 499 200 0 287 428 386 315 299 216 416 489 186'

sl = s.split(' ')
for i in range(len(sl)):
	sl[i] = int(sl[i])
sl.sort()

s = ''
for i in sl:
	s = s + str(i) + ' '

abc = []

#step 1
for i in sl:
	if int(i) in rtable:
		abc.append(rtable[int(i)])
abc.remove('')
abc = abc
tbl = set([i for i in abc])

#step 2..n
while(len(abc)):
	tmp = []
	for i in abc:
		for j in tbl:
			v = spectr(i+j).split(' ')
			v.remove('')
			v = map(int, v)
			v.sort()
			isec = intersection([t for t in sl], [t for t in v])
			v1 = subspectr(i+j).split(' ')
			v1.remove('')
			v1 = map(int, v1)
			v1.sort()
			subisec = intersection([t for t in sl], [t for t in v1])
			if isec == sl:
				print i+j,
			elif subisec == v1:
				tmp.append(i+j)
	abc = [i for i in tmp]