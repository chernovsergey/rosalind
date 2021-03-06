#!/usr/bin/env python

ans = {}

def peptides_with_giving_mass(mass):
    masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129,
              131, 137, 147, 156, 163, 186]

    if mass == 0:
        return 1

    if mass < 0:
        return 0

    if mass in ans:
        return ans[mass]

    result = 0
    for element_mass in masses:
        result += peptides_with_giving_mass(mass - element_mass)

    ans[mass] = result
    return result



mass = 8840

print peptides_with_giving_mass(mass)