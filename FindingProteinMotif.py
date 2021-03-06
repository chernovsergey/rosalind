__author__ = 'Sergey'

import re
import sys
from StringIO import StringIO
from Bio import SeqIO
import requests

if __name__ == '__main__':
    fid = open('FindingProteinMotif.txt', 'r')
    accs = fid.read().strip().split('\n')
    for acc in accs:
        r = requests.get('http://www.uniprot.org/uniprot/%s.fasta' % acc)
        s = SeqIO.read(StringIO(r.text), 'fasta')
        mos = [x for x in re.finditer(r'(?=(N[^P][ST][^P]))', str(s.seq))]
        if not len(mos):
            continue
        print(acc)
        print(' '.join([str(mo.start(0) + 1) for mo in mos]))