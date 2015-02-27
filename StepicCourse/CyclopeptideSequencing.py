__author__ = 'Sergey'
import itertools

f = open("cyclopeptide_sequencing.txt").readline()
Spectrum = f.split(' ')
#f = filter(lambda x: 186 >= int(x) > 0, f)
result = ""
alphabet = "AEDLRPQHMISTKNFWCYVG"
length = 0
candidates = []
_list = list("")
while _list.__len__() != 0:
    length += 1
    _list = itertools.product(alphabet,repeat=length)
    for i in _list:
        pass