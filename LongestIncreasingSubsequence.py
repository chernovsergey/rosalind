import bisect


def LIS(A):
    N = len(A)
    m = [0] * N
    for x in range(N - 2, -1, -1):
        for y in range(N - 1, x, -1):
            if A[x] < A[y] and m[x] <= m[y]:
                m[x] += 1

    max_value = max(m)

    result = []
    for i in range(N):
        if max_value == m[i]:
            result.append(A[i])
            max_value -= 1

    return result


def LDS(A):
    N = len(A)
    m = [0] * N
    for x in range(N - 2, -1, -1):
        for y in range(N - 1, x, -1):
            if m[x] <= m[y] and A[x] > A[y]:
                m[x] = m[y] + 1

    max_value = max(m)

    result = []
    for i in range(N):
        if max_value == m[i]:
            result.append(A[i])
            max_value -= 1

    return result

# We want a maximum function which accepts a default value
from functools import partial, reduce

maximum = partial(reduce, max)


def patience_sort(xs):
    pile_tops = list()
    for x in xs:
        pile = bisect.bisect_left(pile_tops, x)
        if pile == len(pile_tops):
            pile_tops.append(x)
        else:
            pile_tops[pile] = x
        yield x, pile


def longest_increasing_subseq_length(xs):
    return 1 + maximum((pile for x, pile in patience_sort(xs)), -1)


def longest_increasing_subsequence(xs):
    # Patience sort xs, stacking (x, prev_ix) pairs on the piles.
    # Prev_ix indexes the element at the top of the previous pile,
    # which has a lower x value than the current x value.
    piles = [[]]  # Create a dummy pile 0

    for x, p in patience_sort(xs):
        if p + 1 == len(piles):
            piles.append([])

        # backlink to the top of the previous pile
        piles[p + 1].append((x, len(piles[p]) - 1))

    # Backtrack to find a longest increasing subsequence
    npiles = len(piles) - 1
    prev = 0
    lis = list()
    for pile in range(npiles, 0, -1):
        x, prev = piles[pile][prev]
        lis.append(x)
    lis.reverse()
    return lis


if __name__ == "__main__":

    data = 0
    N = 0
    main_seq = 0
    with open('longest_increasing_subsequence.txt') as file:
        data = file.readlines()
        N = int(data[0])
        main_seq = str(data[1]).split()
        main_seq = map(int, main_seq)

    assert (N == len(main_seq))

    lis = LIS(main_seq)
    lds = LDS(main_seq)

    for i in lis:
        print int(i),

    print

    for j in lds:
        print int(j),
