lst = list(filter(lambda x : x % 2, list(map(int, input().split()))))
print(min(lst) if lst else 0)
