def check(n):
    a = [] #khoi tao danh sach de luu
    d = 2
    while d*d <= n:
        cnt = 0
        while n%d == 0:
            n//=d
            cnt+=1
        if cnt > 0:
            a.append((d,cnt))
        d += 1
    if n > 1:
        a.append((n,1))
    return a
t = int(input())
for _ in range(t):
    n = int(input())
    res = ["1"]
    for p, ret in check(n):
        res.append(f"{p}^{ret}")
    print(" * ".join(res)) # dung de noi