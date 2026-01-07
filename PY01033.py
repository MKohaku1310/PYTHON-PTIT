import math
l,r = map(int, input().split())

res = []
for a in range(l,r+1):
    for b in range(a+1,r+1):
        if math.gcd(a,b) != 1:
            continue
        for c in range(b+1,r+1):
            if math.gcd(a,c) == 1 and math.gcd(b,c) == 1:
                res.append((a,b,c))
for t in res:
    print(f"({t[0]}, {t[1]}, {t[2]})")