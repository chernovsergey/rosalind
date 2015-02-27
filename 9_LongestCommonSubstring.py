"""
Class containing SuffixArray functionalities
"""


class SuffixArray:
    # Initializing variables and calculating suffix array for given string
    def __init__(self, s):
        #print s
        #print len(s)
        self.s = s
        self.N = len(self.s)
        self.P = []
        self.suffixes = []
        self.lcp = []

        self.P.append([0 for i in range(self.N)])
        for i in range(self.N):
            self.P[0][i] = ord(self.s[i])

        skip = 1
        level = 1
        while skip < self.N:
            self.P.append([0 for i in range(self.N)])
            M = []
            for i in range(self.N):
                first = self.P[level - 1][i]
                second = self.P[level - 1][i + skip] if ((i + skip) < self.N) else -1000
                M.append((first, second, i))
            M.sort()
            #M.sort(key = cmp_to_key(compare), reverse = True)
            for i in range(self.N):
                if (i > 0) and (M[i][0] == M[i - 1][0]) and (M[i][1] == M[i - 1][1]):
                    self.P[level][M[i][2]] = self.P[level][M[i - 1][2]]
                else:
                    self.P[level][M[i][2]] = i
            skip *= 2
            level += 1

        # Calculate sorted suffix array
        for i in range(self.N):
            self.suffixes.append((self.P[len(self.P) - 1][i], i))
        self.suffixes.sort()
        # Calculate LCP array
        self.lcp.append((0, 0))
        for i in range(1, self.N):
            self.lcp.append((i, self.longestCommonPrefix(self.suffixes[i - 1][1], self.suffixes[i][1])))

    # Returns sorted suffix array
    def getSuffixArray(self):
        return self.suffixes

    # Returns size of suffix array
    def getSize(self):
        return self.N

    # Returns the longest common prefix among s[i....N-1] and s[j....N-1]
    def longestCommonPrefix(self, i, j):
        l = 0
        if i == j:
            return l - i
        k = len(self.P) - 1
        while (k >= 0) and (i < self.N) and (j < self.N):
            if self.P[k][i] == self.P[k][j]:
                i += 1 << k
                j += 1 << k
                l += 1 << k
            k -= 1
        return l

    def getLcpArray(self):
        return self.lcp


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


string_end_mark = ""


def check(d):
    for k in d.keys():
        if d[k] == 0:
            return False
    return True


def longest_common_substring(strings):
    ans = ""
    s = ""
    track = []
    d = {}
    for i in range(len(strings)):

        s += strings[i]
        d[i] = 0

        for j in range(len(strings[i])):
            track.append(i)

        s += string_end_mark + str(i)
        for j in range(len(str(i))):
            track.append(-1)

    sa = SuffixArray(s)
    arr = sa.getSuffixArray()
    lcp = sa.getLcpArray()
    sa_size = sa.getSize()

    start = 0
    while track[arr[start][1]] == -1:
        start += 1
    d[track[arr[start][1]]] += 1
    end = start + 1
    d[track[arr[end][1]]] += 1
    while (check(d) == False) and end < sa_size:
        end += 1
        d[track[arr[end][1]]] += 1

    ans_len = 0
    ans_start = start
    while (start < sa_size) or (end < sa_size):
        if end < sa_size:
            l = sa.longestCommonPrefix(arr[start][1], arr[end][1])
        else:
            l = sa.longestCommonPrefix(arr[start][1], arr[end-1][1])
        if l > ans_len:
            ans_len = l
            ans_start = start
        d[track[arr[start][1]]] -= 1
        start += 1
        while (check(d) ==  False) and (end < sa_size):
            end += 1
            if end < sa_size:
                d[track[arr[end][1]]] += 1
        if end == sa_size and check(d) == False:
            break
    return s[arr[ans_start][1]:arr[ans_start][1]+ans_len], ans_len


if __name__ == "__main__":
    names, strands = extractData("lcs.txt")
    answer, length = longest_common_substring(strands)
    print answer