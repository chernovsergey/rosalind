__author__ = 'Sergey'
import re

def extractData(fname):
    Names, Strands = [], []
    summary_strand = str("")
    f = open(fname, 'r')
    for line in f.read().split('\n'):
        if line.startswith('>'):
            Names.append(line.replace('>', ''))
            summary_strand += "-"
        else:
            summary_strand += line
    f.close()
    Strands = summary_strand.split("-")
    Strands = [x for x in Strands if len(x) != 0]
    return Names, Strands

def reverseComplementary(dna):
    complementary = {
        'A': 'T',
        'C': 'G',
        'T': 'A',
        'G': 'C'
    }
    complemented = [complementary[nt] for nt in dna]
    return ''.join(nt for nt in reversed(complemented))


def RNAtoPROTEIN(rna_string):
    RNAstr = rna_string
    result = ""
    #prepare RNA codon
    #_____________________________________________
    f = open('RNAcodon.txt', 'r').read().splitlines()
    f1 = []
    Dict = {}
    for i in range(0, len(f)):      #split by TAB
        f1.append(f[i].split('\t'))
    for j in range(0, len(f1)):     #remove empty items
        f1[j] = [x for x in f1[j] if x != '']
    for i in range(0, len(f1)):
        for j in range(0, len(f1[i])):
            tmp = f1[i][j]
            Dict.update({tmp[:3]: tmp[4:]})

    #Make Protein acid
    for i in range(0, len(RNAstr)-3 + 1, 3):
        tmp = RNAstr[i:i+3]
        val = Dict.get(tmp)
        result = result + val
    #print(result)
    return result


def get_k_mers_from_dna(genome, k):
    k_mers = []
    for i in range(len(genome) - k + 1):
        k_mers.append(genome[i: i + k])
    return k_mers

names, strands = extractData("peptide_encoding.txt")
peptide = names[0]
genome = strands[0]
k_mers = get_k_mers_from_dna(genome, len(peptide) * 3)
reversed_k_mers = get_k_mers_from_dna(reverseComplementary(genome), len(peptide) * 3)

k_mers = [re.sub('T', 'U', x) for x in k_mers]
reversed_k_mers = [re.sub('T', 'U', x) for x in reversed_k_mers]

for i in k_mers:
    protein = RNAtoPROTEIN(i)
    if protein == peptide:
        print re.sub('U','T', i)
for j in reversed_k_mers:
    protein = RNAtoPROTEIN(j)
    if protein == peptide:
        print reverseComplementary(re.sub('U','T', j))