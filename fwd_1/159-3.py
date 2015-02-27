import sys
from collections import defaultdict

def load(path):
	f = open(path, "r")
	table = f.read().split('\n')
	abc = table[0].split(' ')
	profile = defaultdict(list)
	l = len(table)
	for i in range(1, l):
		arr = table[i].split(' ')
		lt = len(arr)
		for j in range(lt):
			profile[abc[j]].append(float(arr[j]))
	return profile

def probability(kmer, profile):
	prob = 0
	l = len(kmer)
	for i in range(l):
		prob = prob + profile[kmer[i]][i]
	return prob

text = 'GCCGAACAGCAGCTATGTTACTTATCCTGGCGGGCTCAACATGTTGGGACATTTGTCTGGTTACTTTAAACCTTAACCCGCGTTTTCAGCATATCCAAGCCAGGTATCTAGATCGATAAGTCGGAATCGTGATTCTGAGTGGCTTCGGTGTTTCAAACACTATTTCTGAAGGGTTTTGGGCGTCTTGCGTGCAGTATCCC'
k = 8

profile =  load("input.txt")

maxProb = -1
out = ''

l = len(text)
for i in range(l-k+1):
	p = probability(text[i:i+k], profile)
	if p > maxProb:
		maxProb = p
		out = text[i:i+k]
print out