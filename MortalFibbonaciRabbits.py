__author__ = 'sergey'


def solve(n, m):
    F = [1, 1]
    for i in range(2, n):
        if i < m:
            F.append(F[i-1]+F[i-2])
        if i == m:
            F.append(F[i-1]+F[i-2]-1)
        if i == m+1:
            F.append(F[i-1]+F[i-2]-1)
        if i > m+1:
            F.append(F[i-1]+F[i-2]-F[i-m-1])


    return F[len(F)-1]


def solve2(n, m):
    F = [1,1]
    for i in range(2, n):
        F.append(F[i-1]+F[i-2])
    print F
    for j in range(0, n):
        if j >= m:
            F[j] -= 2**(j-m)

    print F

    return F[len(F)-1]


if __name__ == '__main__':
    with open('MortalFibbonaciRabbits.txt') as f:
        data = f.read().strip().split()
        n, m = map(int, data)
        print solve(n, m)
