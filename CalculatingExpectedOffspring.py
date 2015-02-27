__author__ = 'sergey'

# The probabilities of corresponding cases is:
# AA-AA  -> 1
# AA-Aa  -> 1
# AA-aa  -> 1
# Aa-Aa  -> 0.75
# Aa-aa  -> 0.5
# aa-aa  -> 0

#For each case containing two offsprings

Pr = [2., 2., 2., 1.5, 1, 0]

with open('calculating_expected_offspring.txt') as f:
    couples = map(int, f.readline().split())

print sum([a * b for a, b in zip(Pr, couples)])
