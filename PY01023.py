t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    res = ["1"]
    i = 2
    tmp = n
    while i*i <= tmp:
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        if cnt > 0:
            res.append(f"{i}^{cnt}")
        i += 1
    if n > 1:
        res.append(f"{n}^1")
    print(" * ".join(res))

