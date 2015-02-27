__author__ = 'Sergey'
import random as rnd
from numpy import zeros
from numpy import matrix
from numpy import arange
from numpy import ravel

def get_data(fname):
    f = open(fname, 'r')
    b = f.read().split('\n')
    b = [x for x in b if len(x) != 0]
    return b


def get_consensus(mat):
    consensus = ""
    for i in mat.T:
        m = max(ravel(i))
        col = (ravel(i)).tolist()
        for j in range(len(col)):
            if col[j] == m:
                if j == 0:
                    consensus += 'A'
                if j == 1:
                    consensus += 'C'
                if j == 2:
                    consensus += 'G'
                if j == 3:
                    consensus += 'T'
    return consensus


def get_profile(k_mers):
    len_of_str = len(k_mers[0])
    mat = matrix(zeros((4, len_of_str), dtype=int))
    columns = []
    for j in range(len_of_str):
        s = ""
        for i in k_mers:
            a = i[j]
            s += a
        columns.append(s)
    for i in range(len(columns)):
        a = str(columns[i]).count('A')
        c = str(columns[i]).count('C')
        g = str(columns[i]).count('G')
        t = str(columns[i]).count('T')
        mat[0, i] = a
        mat[1, i] = c
        mat[2, i] = g
        mat[3, i] = t
    return get_consensus(mat)


def get_k_strings(_set, indexes, k):
    result = []
    for i in xrange(len(_set)):
        _from = indexes[i]
        _to = indexes[i] + k
        result.append(_set[i][_from: _to])
    return result


def get_motifs(profile, dna):
    pass


def random_motif_search(dna, k, t):
    _k = k
    _t = t
    _DNA = dna
    indexes = [int(rnd.randint(1, _k)) for i in arange(_t)]
    bestMotifs = []

    Motifs = get_k_strings(_DNA, indexes, k)
    bestMotifs = bestMotifs
    while True:
        _profile = get_profile(Motifs)




k_mers = get_data("rms.txt")
random_motif_search(k_mers, 4, 5)