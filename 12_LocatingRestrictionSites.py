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


def getReverse(_str):
    return str(_str)[::-1]


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


names, strands = extractData("reverse_palindrome.txt")
# if dna strand is equal to reverse complementary strand,
# then it's reverse palindrome
aligns = []
indexes = []
_len = len(strands[0])

for i in xrange(_len):
    sub = strands[0][i:i + 12]
    aligns.append(sub)
    for j in xrange(len(sub)):
        tmp = sub[0:len(sub) - j]
        aligns.append(tmp)

#aligns = dict(zip(aligns, aligns)).values()
aligns = [e for i, e in enumerate(aligns) if e not in aligns[:i]]
#print aligns
#print len(aligns)

for each in aligns:
    if 4 <= len(each) <= 12:
        if isReversePalindrome(each):
            pattern = '(?=' + (str(each)) + ')'
            matches = [m.start() for m in re.finditer(pattern, strands[0])]
            for i in matches:
                print int(i + 1), len(each)