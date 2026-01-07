import math

def ngto(n):
    if n < 2: return False
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0: return False
    return True
def Sum(n):
    sum = 0
    s = str(n)
    for i in range (len(s)):
        sum += int(s[i])
    return sum

t = int(input().strip())
for _ in range(t):
    a,b = map(int, input().split())
    d = math.gcd(a,b)
    c = Sum(d)
    if ngto(c): print('YES')
    else: print('NO')