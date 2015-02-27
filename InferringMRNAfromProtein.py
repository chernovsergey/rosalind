__author__ = 'sergey'

from collections import defaultdict
from operator import mul


def problem(dataset = None):
    if not dataset:
        dataset = open("kmp.txt").read().strip()

    amino_acids = defaultdict(list)
    with open("RNAcodon.txt") as f:
        for line in f:
            if not line.strip():
                continue
            codon, aa = line.strip().split()
            if aa == 'Stop':
                aa = None
            amino_acids[aa].append(codon)

    pool = [amino_acids[aa] for aa in dataset] + [amino_acids[None]]
    return reduce(mul, map(len, pool))


if __name__ == '__main__':
    argument = problem()
    result = argument % 1000000
    print result
