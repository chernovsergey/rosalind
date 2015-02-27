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
    for i in range(0, len(RNAstr) - 3, 3):
        tmp = RNAstr[i:i + 3]
        val = Dict.get(tmp)
        result = result + val
    return result


def getProtein(coddon):
    DNA_CODON_TABLE = {
        'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
        'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
        'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
        'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
        'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
        'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
        'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
        'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
        'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
        'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
        'TAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
        'TAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
        'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
        'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
        'TGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
        'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
    }
    if DNA_CODON_TABLE.has_key(coddon):
        return DNA_CODON_TABLE[coddon]
    else:
        return ''


def reverseComplementary(dna):
    complementary = {
        'A': 'T',
        'C': 'G',
        'T': 'A',
        'G': 'C'
    }
    complemented = [complementary[nt] for nt in dna]
    return ''.join(nt for nt in reversed(complemented))


def find_possible_orf(s):
    main_str = s
    indices = []
    protein_string = ''
    result = []

    # All indices of AUG in RNA
    for i in range(len(main_str)):
        protein = getProtein(main_str[i:i + 3])
        if protein and protein == 'M':
            indices.append(i)

    # For all AUG find possible protein strings
    for i in indices:
        found_stop_coddon = False
        protein_string = ''

        for j in range(i, len(main_str), 3):
            protein = getProtein(main_str[j:j + 3])

            if not protein:
                break
            if protein == 'Stop':
                found_stop_coddon = True
                break

            protein_string += protein

        if found_stop_coddon:
            result.append(protein_string)
    return result


names, strands = extractData("ORF.txt")
set_one = find_possible_orf(strands[0])
reverse_comp = reverseComplementary(strands[0])
set_two = find_possible_orf(reverse_comp)

print "\n".join(set(set_one + set_two))