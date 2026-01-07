def ngto(n):
    if n < 2: return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: return False
    return n > 1
t = int(input().strip())
for _ in range(t):
    s = input().strip()
    d = s[-4:]
    if ngto(int(d)): print('YES')
    else: print('NO')