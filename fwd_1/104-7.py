import math, itertools

s = "0 71 71 103 128 129 137 142 147 163 174 186 199 245 266 270 276 289 291 300 333 360 362 373 413 428 429 431 433 436 462 499 507 536 557 559 565 570 576 578 599 628 636 673 699 702 704 706 707 722 762 773 775 802 835 844 846 859 865 869 890 936 949 961 972 988 993 998 1006 1007 1032 1064 1064 1135"
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
i = 1
while spectr[i] < 187:
    if rever_dict.get(spectr[i], 0) != 0:
        if rever_dict[spectr[i]] not in begin_prot:
            begin_prot.append(rever_dict[spectr[i]])
        spectr.remove(spectr[i])
    else:
        i+=1
#print spectr
print begin_prot
def mass(prot):
    return sum([dic[i] for i in prot])
def printMass(prot):
    return "-".join([str(dic[i]) for i in prot])

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
    if len(tmp) == 0:
        for i in prot:
            print printMass(i),
    prot = list(tmp)
    iter += 1
