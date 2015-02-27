
dic = {'G': 57 ,    'A': 71,    'S': 87,    'P': 97,    'V': 99,    'T': 101,   'C': 103,   'I': 113,   'L': 113,   'N': 114,   'D': 115,   'K': 128,
       'Q': 128,    'E': 129,   'M': 131,   'H': 137,   'F': 147,   'R': 156,   'Y': 163,   'W': 186,   '' : 0 }


s = "YTCCEHWVEHSWYD"
dd = []
def getCyclicSubstr(s):
    ss = s*2
    len_s = len(s)
    dd.append(s)
    dd.append('')
    while len_s-1:
        for i in xrange(len(s)):
            dd.append(ss[i:i+len_s-1])
        len_s -= 1

getCyclicSubstr(s)

list_res = []
for i in dd:
    res = 0
    for j in xrange(len(i)):
        res += dic[i[j]]
    list_res.append(res)

for i in sorted(list_res):
    print i,
print
print len(list_res)