t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ls, s = [1, 2], 2
    while(ls[-1]+ls[-2] <= n):
        ls.append(ls[-1]+ls[-2])
        if ls[-1]%2 == 0:
            s += ls[-1]
    print(s)
