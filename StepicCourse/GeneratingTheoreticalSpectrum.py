__author__ = 'Sergey'

mass_table = {
    "G": 57,
    "A": 71,
    "S": 87,
    "P": 97,
    "V": 99,
    "T": 101,
    "C": 103,
    "I": 113,
    "L": 113,
    "N": 114,
    "D": 115,
    "K": 128,
    "Q": 128,
    "E": 129,
    "M": 131,
    "H": 137,
    "F": 147,
    "R": 156,
    "Y": 163,
    "W": 186
}


def get_all_substrings_in_cyclic_peptide(main_string):

    substrings = []
    for i in range(1, len(main_string)/2 + 1):
        for j in range(0, len(main_string)/2):
            substrings.append(main_string[j:j+i])
            if i == len(main_string)/2:
                break
    return substrings


def get_cyclospectrum(collection):
    mass_collection = [0]
    for element in collection:
        val = 0
        for j in range(len(element)):
            char = element[j]
            mass_char = mass_table[char]
            val += mass_char
        mass_collection.append(val)
    return sorted(mass_collection)


main_str = 2 * "GIQRWQRPVFRIGKG"
collection = get_all_substrings_in_cyclic_peptide(main_str)
line = get_cyclospectrum(collection)
stringa = ""
for elem in line:
    stringa += str(elem)
    stringa += " "
print stringa