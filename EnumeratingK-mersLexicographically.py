__author__ = 'Sergey'
from itertools import product


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


if __name__ == "__main__":
    names, strands = extractData("enumerating_k-mers.txt")
    all = strands[0].replace(' ', '')
    alphabet = all[:4]
    number = int(all[-1])
    k_mers = product(alphabet, repeat=number)
    for i in k_mers:
        row = ""
        for j in range(len(i)):
            row += str(i[j])
        print row
