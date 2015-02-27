__author__ = 'Sergey'


def extractData(fname):
    Names, Strands = [], []
    summary_strand = str("")
    f = open(fname, 'r')
    for line in f.read().split('\n'):
        if line.startswith('>'):
            Names.append(line.replace('>', ''))
            summary_strand += "-"
        else:
            summary_strand += line
    f.close()
    Strands = summary_strand.split("-")
    Strands = [x for x in Strands if len(x) != 0]
    return Names, Strands


def RNAtoPROTEIN(rna_string):
    RNAstr = rna_string
    result = ""
    #prepare RNA codon
    #_____________________________________________
    f = open('RNAcodon.txt', 'r').read().splitlines()
    f1 = []
    Dict = {}
    for i in range(0, len(f)):      #split by TAB
        f1.append(f[i].split('\t'))
    for j in range(0, len(f1)):     #remove empty items
        f1[j] = [x for x in f1[j] if x != '']
    for i in range(0, len(f1)):
        for j in range(0, len(f1[i])):
            tmp = f1[i][j]
            Dict.update({tmp[:3] : tmp[4:]})

    #Make Protein acid
    for i in range(0, len(RNAstr)-3,3):
        tmp = RNAstr[i:i+3]
        val = Dict.get(tmp)
        result = result + val
    #print(result)
    return result

names, strands = extractData("protein_translation.txt")
print RNAtoPROTEIN(strands[0])