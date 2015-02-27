__author__ = 'Sergey'
import itertools
import sys
import string

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


def count(genome, pattern, num_mismatches):
        i = 0
        count_p = 0
        while i <= len(genome) - len(pattern):
                indx = i
                count = 0
                for j in range(0, len(pattern)):
                        if genome[indx] == pattern[j]:
                                count = count + 1
                        indx = indx + 1
                if count >= len(pattern) - num_mismatches:
                        count_p = count_p + 1

                i = i + 1
        return count_p

#names, strands = extractData("frequent_words_with_mismatches.txt")

#nums = strands[0][-3:].replace(' ', '')
#sequence = strands[0][:-3]
#kmer_size = int(nums[0])
#num_mismatches = int(nums[1])
#
#print "Read sequence = " + sequence
#
#print "K-mer size = ", kmer_size
#
#print "Max mismatches = ", num_mismatches


def get_freq_words_with_mismatches(k, d, dna):
    result = []
    seq = "ATCG"
    list_pattern = itertools.product(seq, repeat=k)
    max_p = 0
    aux = 0
    list_max = []

    for p in list_pattern:
            aux = count(dna, p, d)
            if aux >= max_p:
                    max_p = aux
                    list_max.append([p, max_p])

    for i in list_max:
        if i[1] == max_p:
            result.append("".join(map(str, i[0])))
    return result