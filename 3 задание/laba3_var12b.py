m = [[10, 10, 10, 10, 10],
     [9, 9, 9, 9, 9],
     [5, 5, 5, 5, 5],
     [4, 4, 4, 4, 4],
     [2, 2, 2, 2, 2], ]

for i in range(len(m) - 1):
    for j in range(len(m[0])):
        m[i][j] -= m[-1][j]

for i in m:
    print(*i)
