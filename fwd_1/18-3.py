import sys

d = {'AUG':'M', 'AUA':'I', 'AUC':'I', 'AUU':'I', 'AGG':'R', 'AGA':'R', 'AGC':'S', 'AGU':'S', 'ACG':'T', 'ACA':'T', 'ACC':'T', 'ACU':'T', 'AAG':'K', 'AAA':'K', 'AAC':'N', 'AAU':'N', 'UUG':'L', 'UUA':'L', 'UUC':'F', 'UUU':'F', 'UGG':'W', 'UGA':'', 'UGC':'C', 'UGU':'C', 'UCG':'S', 'UCA':'S', 'UCC':'S', 'UCU':'S', 'UAG':'', 'UAA':'', 'UAC':'Y', 'UAU':'Y', 'GUG':'V', 'GUA':'V', 'GUC':'V', 'GUU':'V', 'GGG':'G', 'GGA':'G', 'GGC':'G', 'GGU':'G', 'GCG':'A', 'GCA':'A', 'GCC':'A', 'GCU':'A', 'GAG':'E', 'GAA':'E', 'GAC':'D', 'GAU':'D', 'CUG':'L', 'CUA':'L', 'CUC':'L', 'CUU':'L', 'CGG':'R', 'CGA':'R', 'CGC':'R', 'CGU':'R', 'CCG':'P', 'CCA':'P', 'CCC':'P', 'CCU':'P', 'CAG':'Q', 'CAA':'Q', 'CAC':'H', 'CAU':'H'}

s = 'GUGAAACUUUUUCCUUGGUUUAAUCAAUAU'
k = len(s)


for t in range(3):
	s1 = s[t:k]
	k1 = len(s1)
	print s1
	for i in range(k1/3):
		ss = s1[i*3:i*3+3]
		sys.stdout.write(d[ss])
	print ''