import sys


def editDistance(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        c[i][0] = i
    for i in range(n+1):
        c[0][i] = i
    for i in range(m):
        for j in range(n):
            c[i+1][j+1] = sys.maxsize
            if x[i] == y[j]:
                # copy
                c[i + 1][j + 1] = c[i][j]
            if x[i] != y[j] and c[i][j]+1 < c[i+1][j+1]:
                # replace
                c[i + 1][j + 1] = c[i][j]+1
            if i >= 1 and j >= 1 and x[i] == y[j-1] and x[i-1] == y[j] and c[i-1][j-1] + 1 < c[i+1][j+1]:
                # exchange
                c[i + 1][j + 1] = c[i-1][j-1] + 1
            if c[i][j+1] + 1 < c[i+1][j+1]:
                # delete
                c[i + 1][j + 1] = c[i][j+1] + 1
            if c[i+1][j] + 1 < c[i+1][j+1]:
                # insert
                c[i + 1][j + 1] = c[i+1][j] + 1
    return c


def distance(x, y):
    c = editDistance(x, y)
    return c[-1][-1]


def ngrams(string, n):
    output = set()
    for i in range(len(string)-n+1):
        output.add(string[i:i+n])
    return output
