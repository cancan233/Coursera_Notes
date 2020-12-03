# Uses python3
def edit_distance(s, t):
    # write your code here
    s, t = "#" + s, "#" + t

    m = len(s)
    n = len(t)

    D = [[0 for j in range(n)] for i in range(m)]

    for i in range(1, m):
        D[i][0] = i
        for j in range(1, n):
            D[0][j] = j
            insertion = D[i - 1][j] + 1
            deletion = D[i][j - 1] + 1
            substitution = D[i - 1][j - 1] + 1
            match = D[i - 1][j - 1]
            if s[i] == t[j]:
                D[i][j] = min(insertion, deletion, match)
            else:

                D[i][j] = min(insertion, deletion, substitution)
    return D[m - 1][n - 1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # print(edit_distance("editing", "distance"))
