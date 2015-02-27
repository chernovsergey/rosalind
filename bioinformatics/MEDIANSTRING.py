import itertools
alphabet = "ACGT"
k = 6

lines = [
"GGGCTCATCACTTGGAAACAAAGACGAACGGGAGAGCAAACC",
"GTTGAATCCATGCAACGAGGTAAGTCACAGGCTTGGTATGAA",
"ACACAACAACGAGAGTCTGCGCGAATTGGATACATCTGTGGG",
"GTATACTCTTAACCACAGTGCGTGGTGCGACAATGATCGCTG",
"CATAACCGCTGGCCTATGCGTATGCAAGGAATTCTTAAGCTC",
"CCACCGGCGCTTCAAAGACACAGATGCGAAAGTAGTGCCGGG",
"GAGTGCGAATCCCAACGAGGATTTTTTCCAGGGTAATACAGG",
"TCTGCGACCTTCATTGACTATCATGAATGAAATATGCAAGGA",
"CAACGATAGCCCTTGTACCCCACCCTGGTCCGCTACCTCCTA",
"GAAAGGTAGTAAACCTCCCTAATTCAATGAGCGCCCCCATGG"

]

def Dist(a, b):
	if len(a) != len(b): print("error in Dist function")
	tmp = 0
	for i in range(len(a)):
		if a[i] != b[i]:
			tmp += 1
	return tmp

def DistInLine(a, line):
	if len(a) > len(line): print("error in DistInLine function")
	bestDist = len(a)
	for i in range(len(line)-len(a)+1):
		if (Dist(a, line[i:i+len(a)]) < bestDist): bestDist = Dist(a, line[i:i+len(a)])
	return bestDist

def DistInDna(a, lines):
	return sum([DistInLine(a, line) for line in lines]) 


allPatterns = [''.join(i) for i in itertools.product(alphabet, repeat = k)]

bestPattern= ""
bestDist = k * len(lines)
for i in allPatterns:
	tmp = DistInDna(i, lines)
	if bestDist > tmp:
		bestDist = tmp
		bestPattern = i
print( bestPattern)

