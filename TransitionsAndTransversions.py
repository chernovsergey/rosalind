__author__ = 'Sergey'

#transversion ==> 0
#transition ==> 1
transitions_and_transversions = {
    "A-G": 1,
    "A-C": 0,
    "A-T": 0,
    "C-A": 0,
    "C-G": 0,
    "C-T": 1,
    "G-A": 1,
    "G-C": 0,
    "G-T": 0,
    "T-A": 0,
    "T-C": 1,
    "T-G": 0
}
num_transversions = 0
num_transitions = 0


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


def what_is_it(sym1, sym2):
    key = str(sym1) + "-" + str(sym2)
    if transitions_and_transversions.has_key(key):
        val = transitions_and_transversions[key]
    else:
        return -1
    return val


if __name__ == "__main__":
    names, strands = extractData("TransAndTrans.txt")
    str1, str2 = strands[0], strands[1]
    for i in range(len(strands[0])):
        action = what_is_it(str1[i], str2[i])
        if action == 0:
            num_transversions += 1
        if action == 1:
            num_transitions += 1
        if action == -1:
            pass
    print float(num_transitions) / num_transversions