def ngto(n):
    if n < 2: return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: return False
    return n > 1
def check(n):
    for i in range(len(n)):
        if ngto(i):
            if not ngto(int(n[i])): return False
        else:
            if ngto(int(n[i])): return False
    return True
t = int(input().strip())
for _ in range(t):
    n = input().strip()
    if check(n): print('YES')
    else: print('NO')