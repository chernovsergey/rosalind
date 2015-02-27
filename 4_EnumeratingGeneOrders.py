from math import factorial
from itertools import combinations_with_replacement
_n = 2
_s = ""
per = factorial(_n)
print per


#creating procedure for permutations
def permutations(items):

    def p(items, n):
        if n == 0:
            yield []
        else:
            for i in range(n):
                for j in p(items[:i] + items[i + 1:], n - 1):
                    yield [items[i]] + j

    return p(items, len(items))


for i in permutations(range(1, _n + 1)):
    A = i
    for j in range(0, len(A)):
        print A[j],
    print
