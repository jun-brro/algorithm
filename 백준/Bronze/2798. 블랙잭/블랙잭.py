n, m = map(int, input().split())
lst = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if lst[i] + lst[j] + lst[k] > m:
                continue
            else:
                result = max(result, lst[i] + lst[j] + lst[k])

print(result)