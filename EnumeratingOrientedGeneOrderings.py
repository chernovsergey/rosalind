__author__ = 'Sergey'
from math import factorial
from itertools import product, permutations, combinations, combinations_with_replacement

def merge_product(product):
    result = []
    possible_numbers, signs = product
    for i, number in enumerate(possible_numbers):
        sign = signs[i]
        number = int(sign + str(number))
        result.append(number)
    return result

n = 6
print factorial(n) * 2 ** n
# Make a set of possible permutations
possible_numbers = list(permutations(range(1, n + 1)))
# Make possible signs
signs = list(product("-+", repeat=n))
# Make a product of previous objects
result = product(possible_numbers, signs)
# Merge results and print
result = map(merge_product,  result)
for r in result:
    print " ".join(map(str, r))




