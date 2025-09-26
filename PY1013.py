import math

def ngto(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True
def check(n):
    return sum(int(d) for d in str(n)) # tra ve tong cua cac chu so trong 1 chuoi
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    g = math.gcd(a,b);
    s = check(g)
    if ngto(s): print("YES")
    else : print("NO")