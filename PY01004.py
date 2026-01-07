import math
def check (n:int):
    s = 0
    for i in range (1,n):
        if math.gcd(i,n) == 1:
            s+=1
    return s

def ngto (n):
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return n>1

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    k = check(n)
    if ngto(k):
        print ('YES')
    else: print('NO')
