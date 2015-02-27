import sys
from collections import defaultdict

s = '0 137 186 323'
#m = 20
#n = 60


def convolution(s):
    sl = s.split(' ')
    for i in range(len(sl)):
        sl[i] = int(sl[i])
    sl.sort()

    cl = defaultdict(int)

    k = len(sl)
    for i in range(k):
        for j in range(i, k):
            if abs(sl[i] - sl[j]) >= 57 and abs(sl[i] - sl[j]) <= 200:
                cl[abs(sl[i] - sl[j])] = cl[abs(sl[i] - sl[j])] + 1
    out = list(cl.items())
    out.sort(key=lambda item: item[1])
    out = out[::-1]
    return out


print convolution(s)