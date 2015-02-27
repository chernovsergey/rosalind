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


def isReversePalindrome(s1):
    return s1 == reverseComplementary(s1)


def return_all_overlaping_matches(pattern, string):
    pattern = '(?=' + (str(pattern)) + ')'
    matches = [m.start() for m in re.finditer(pattern, string)]
    return matches


def get_hamming_distance(str1, str2):
    dist = 0
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                dist += 1
    return dist


def approximate_pattern_matching(pattern, string, mismatches):
    _p = pattern
    _s = string
    _l = len(pattern)
    _miss = mismatches
    positions = []
    for i in range(len(string) - _l + 1):
        substr = _s[i:i+_l]
        dist = get_hamming_distance(substr, _p)
        if dist <= _miss:
            positions.append(i)
    return positions

names, strands = extractData("pattern_matching.txt")
pattern = names[0]
string = strands[0]
miss = int(names[1])
result = approximate_pattern_matching(pattern, string, miss)
s = ""
for r in result:
    s += str(r)
    s += " "
print s