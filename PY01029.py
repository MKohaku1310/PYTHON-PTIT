import math
t = int(input().strip())

for _ in range(t):
    n = input().strip()
    s = n[::-1]
    a = int(n)
    b = int(s)
    if math.gcd(a,b) == 1: print('YES')
    else: print('NO')