def check(n):
    s = str(n)
    if len(s) % 2 != 0: return False
    if s != s[::-1]: return False
    for ch in s:
        if ch not in '02468':
            return False
    return True

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    res = []
    for i in range(22,n):
        if check(i): res.append(i)
    print(*res)