import sys

d = {'AUG':'M', 'AUA':'I', 'AUC':'I', 'AUU':'I', 
	 'AGG':'R', 'AGA':'R', 'AGC':'S', 'AGU':'S', 
	 'ACG':'T', 'ACA':'T', 'ACC':'T', 'ACU':'T', 
	 'AAG':'K', 'AAA':'K', 'AAC':'N', 'AAU':'N', 
	 'UUG':'L', 'UUA':'L', 'UUC':'F', 'UUU':'F', 
	 'UGG':'W', 'UGA':'', 'UGC':'C', 'UGU':'C', 
	 'UCG':'S', 'UCA':'S', 'UCC':'S', 'UCU':'S', 
	 'UAG':'', 'UAA':'', 'UAC':'Y', 'UAU':'Y', 
	 'GUG':'V', 'GUA':'V', 'GUC':'V', 'GUU':'V', 
	 'GGG':'G', 'GGA':'G', 'GGC':'G', 'GGU':'G', 
	 'GCG':'A', 'GCA':'A', 'GCC':'A', 'GCU':'A', 
	 'GAG':'E', 'GAA':'E', 'GAC':'D', 'GAU':'D', 
	 'CUG':'L', 'CUA':'L', 'CUC':'L', 'CUU':'L', 
	 'CGG':'R', 'CGA':'R', 'CGC':'R', 'CGU':'R', 
	 'CCG':'P', 'CCA':'P', 'CCC':'P', 'CCU':'P', 
	 'CAG':'Q', 'CAA':'Q', 'CAC':'H', 'CAU':'H'}

def reverse(s):
	d = {'A':'T', 'G':'C', 'T':'A', 'C':'G'}
	s = s[::-1]
	out = ''
	for i in s:
		out = out + d[i]
	return out

def encode(s):
	l = len(s)
	out = ''
	for i in range(l/3):
		out = out + d[s[i*3:i*3+3].replace('T', 'U')]
	return out


s = 'CGAGATCCACA'
ss = 'TTG'

k = len(s)
sk = len(ss)
for i in range(k-sk*3):
	tmp = encode(s[i:i+sk*3])
	tmp1 = encode(reverse(s[i:i+sk*3]))
	if tmp == ss or tmp1 == ss:
		print s[i:i+sk*3]