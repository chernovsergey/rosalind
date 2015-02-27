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


#data to dictionary example
def toDict(_keys, _values):
    d = {}.fromkeys(_keys)
    if len(_keys) == len(_values):
        for x in xrange(len(_keys)):
            d[_keys[x]] = _values[x]
    return d


def buildOverlapRelations(names, strands, const):
    a = []
    for i in xrange(len(strands)):
        for j in xrange(len(strands)):
            if strands[i] != strands[j]:
                x = strands[i][len(strands[i]) - const:]
                y = (strands[j])[:const]
                if x == y:
                    b = [names[i], names[j]]
                    a.append(b)
    for i in xrange(len(a)):
        print a[i][0], a[i][1]


names, strands = extractData("99_overlapG.txt")
buildOverlapRelations(names,strands,3)