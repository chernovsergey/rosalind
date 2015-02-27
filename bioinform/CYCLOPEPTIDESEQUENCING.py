import math, itertools

s = "0 71 99 99 113 128 147 147 163 170 199 212 246 246 275 276 298 310 317 346 359 374 375 409 423 445 445 445 480 487 522 522 522 544 558 592 593 608 621 650 657 669 691 692 721 721 755 768 797 804 820 820 839 854 868 868 896 967"
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
