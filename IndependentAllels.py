from scipy.special._ufuncs import binom

__author__ = 'sergey'


def P(n, k):
    return binom(2 ** k, n) * 0.25 ** n * 0.75 ** (2 ** k - n)


def Solve(n, k):
    return 1 - sum([P(n, k) for n in range(N)])


if __name__ == '__main__':
    data = 0
    k = 0
    N = 0
    with open('IndependentAlleles.txt') as f:
        data = f.read().strip().split()
        k, N = map(int, data)

    print k, N

    print round(Solve(N, k), 3)