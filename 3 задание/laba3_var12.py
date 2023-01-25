arr = [[-1, 1, 2, 2], [1, -7, 8, 1], [2, 2, 4, 1], [2, 1, 3, 6]]
for i in arr :
    print(*map('{:2d}'.format, i))
print()
n = 4
arr_rev = list(map(list,zip(*arr)))
for i in range(n) :
    for j in range(n) :
        if arr[i] == arr_rev[j] :
            print(i+1, 'строка и ', j+1, 'столбец равны')
