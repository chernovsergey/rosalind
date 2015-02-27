from functools import reduce

text = "AAGCTGGCGGCATGCGGCATCCCTAGTACTTGTAGCGCCGGACTGGCGTGGCCAGGCTATAGTTGGTCGGAACTCACGTGGTCGCGAACCAGTGCAAACCGAAGTCTGAGGAAACCCCGATAAATGTGGTCACCGCCCACCAAAAGGCAGATGGCGGGCGCAGCCTTCGTCCAACAATTCGTGGTAAAATTAAGTTCAAG"
k = 8

profile = [
    [0.24, 0.24, 0.32, 0.2],
    [0.28, 0.2, 0.2, 0.32],
    [0.16, 0.2, 0.36, 0.28],
    [0.24, 0.12, 0.44, 0.2],
    [0.32, 0.24, 0.24, 0.2],
    [0.36, 0.36, 0.16, 0.12],
    [0.2, 0.32, 0.24, 0.24],
    [0.28, 0.16, 0.24, 0.32]
]


def probability(pattern, profile):
    d = dict()
    d['A'] = 0
    d['C'] = 1
    d['G'] = 2
    d['T'] = 3
    tmp = 1
    for i in range(k): tmp *= profile[i][d[pattern[i]]]
    return tmp


def BestPattern(text, k):
    max_probability = 0
    best_pattern = ""
    for i in range(len(text) - k + 1):
        tmp = probability(text[i:i + k], profile)
        if tmp > max_probability:
            max_probability = tmp
            best_pattern = text[i:i + k]
    return best_pattern


print(BestPattern(text, k))

