t = int(input())
for _ in range(t):
    s = input().strip()
    n = input().strip()
    cnt = 0
    i = 0
    l = len(n)
    while i <= len(s) - l:
        if s[i:i+l] == n:
            cnt += 1
            i += l
        else:
            i += 1
    print(cnt)
