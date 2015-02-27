import sys

s = 'AAAACCCGGT'

d = {'A':'T', 'G':'C', 'T':'A', 'C':'G'}

s = s[::-1]
tmp = ''
for i in s:
	tmp = tmp + d[i]
	sys.stdout.write(d[i])
print '\n' + tmp