import math, itertools

s = "483 1111 99 186 128 355 1480 811 1064 1296 468 370 425 129 899 771 1239 184 908 441 572 911 256 799 981 938 0 227 997 553 1239 101 682 939 983 795 156 810 569 312 1125 1281 1294 227 541 1223 570 369 1381 230 709 685 542 128 314 1040 386 1166 936 1165 241 1351 782 1012 756 1211 910 1367 927 369 1110 199 1037 416 1324 1094 413 643 257 312 798 884 1039 884 1111 269 1250 581 340 113 1253 1012 71 596 128 1168 669 1379 1140 544 724 700 1409 1168 355 912 698 499 128 813 1352 670 1352 440 568 1224 1352 1367 113 443 667 1125 1253 1067 1352 681 780 497 241 596 315 1055 468 837"
spectr = sorted(map(int, s.split(" ")))

print (1 + math.sqrt(1+4*(len(spectr)-2)))/2.0
N = int(math.ceil((1 + math.sqrt(1+4*(len(spectr)-2)))/2))

dic = { 'G': 57 ,    'A': 71,    'S': 87,
        'P': 97,     'V': 99,    'T': 101,
        'C': 103,       'L': 113,
        'N': 114,    'D': 115,   'K': 128,    'E': 129,   'M': 131,
        'H': 137,    'F': 147,   'R': 156,
        'Y': 163,    'W': 186,   '' : 0 }

rever_dict = {}
for i in dic:
    rever_dict[dic[i]] = i

begin_prot = []
alfabet = sorted(map(int, "128 113 241 227 312 468 156 355 369 71 99 15".split(" ")))
i = 1
for i in alfabet:
    if rever_dict.get(i, 0) != 0:
        if rever_dict[i] not in begin_prot:
            begin_prot.append(rever_dict[i])

#print spectr
print begin_prot
def mass(prot):
    return sum([dic[i] for i in prot])

prot = list(begin_prot)
k = 5
iter = 1
while len(prot):
    tmp = []
    for i in prot:
        for j in begin_prot:
            if mass(i+j) in spectr and i[1:]+j in prot:
                if i+j not in tmp:
                    tmp.append(i+j)
            if mass(i+j) == max(spectr):
                print i+j
                exit(0)
    if len(tmp) == 0:
        for i in prot:
            print i,
    prot = list(tmp)
  #  print iter, len(tmp)
   # print prot
    iter += 1
