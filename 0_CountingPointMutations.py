dna_1 = ""
dna_2 = ""
count = 0
if len(dna_1) == len(dna_2):
    for i in range(0, len(dna_1)):
        if dna_1[i] != dna_2[i]:
            count += 1

    print count
