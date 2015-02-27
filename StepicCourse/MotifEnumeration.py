__author__ = 'Sergey'
import re
import itertools


def get_k_mers_from_dna(genome, k):
    k_mers = []
    for i in range(len(genome) - k + 1):
        k_mers.append(genome[i: i + k])
    return k_mers


def intersect(a, b):
    return list(set(a) & set(b))


def get_hamming_distance(str1, str2):
    dist = 0
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                dist += 1
    return dist


def min_pattern_matching(pattern, string, mismatches):
    matches = []
    ok_value = int(len(pattern) - mismatches)
    _p = pattern
    _s = string
    _l = len(pattern)
    for i in range(len(string) - _l + 1):
        substr = _s[i:i+_l]
        dist = get_hamming_distance(substr, _p)
        if dist <= ok_value:
            matches.append(dist)
    if len(matches) != 0:
        return min(matches)
    else:
        return len(pattern)


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

f = open("motifenumeration.txt").readlines()
f = [re.sub('\n', '', x) for x in f]
k_value = int(f[0][1])
d_value = int(f[0][3])
dna = f[1:]
k_mers_list = []
union_set = []

#build most frequent k-mers from each string in set
for each_string in dna:
    tmp_set = get_freq_words_with_mismatches(k_value, d_value, each_string)
    k_mers_list.append(tmp_set)
for x in k_mers_list:
    union_set += x

#checking appears motifs in every string with at most d mistmatches
for each_motif in union_set:
    for each_string in dna:
        tmp = min_pattern_matching(each_motif, each_string, d_value)
print union_set