from math import log10
__author__ = 'sergey'


def get_string_content(s):
    d = [0, 0]
    for sym in s:
        if sym in ['A', 'T']:
            d[1] += 1
        elif sym in ['G', 'C']:
            d[0] += 1
    return d


def probability(str_content, gc_prob):
    pr_g_or_c = gc_prob / 2.
    pr_a_or_t = (1 - gc_prob) / 2.
    assert (2 * pr_g_or_c + 2 * pr_a_or_t == 1.0)
    return pr_g_or_c ** str_content[0] * pr_a_or_t ** str_content[1]


def problem(s, arr):
    output = []
    content = get_string_content(s)
    for i in arr:
        output.append(log10(probability(content, i)))
    return output


if __name__ == '__main__':
    S = ''
    A = []
    with open('kmp.txt') as f:
        tmp = f.readlines()
        S = tmp[0].strip()
        A = map(float, str(tmp[1]).split(' '))
        del tmp

    B = problem(S, A)
    for i in B:
        print i,