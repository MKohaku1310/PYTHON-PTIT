import math
for t in range(int(input())):
    n = input().strip()
    nd = ''.join(reversed(n))
    n = int(n)
    nd = int(nd)
    if math.gcd(n,nd) == 1 : print('YES')
    else : print('NO')
