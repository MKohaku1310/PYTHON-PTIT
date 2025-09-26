import math
def gcd1(a,b):
    b1 = 0
    for d in b:
        b1 = (b1*10+int(d)) % a
    return math.gcd(a,b1)

t = int(input())
for _ in range(t):
    a = int(input())
    b = input()
    print(gcd1(a,b))