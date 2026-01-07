def ngto(n):
    if n < 2: return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: return False
    return n > 1

def check(n):
    sum = 0
    for i in range(len(n)):
        if i % 2 == 0 and int(n[i]) % 2 != 0: return False
        if i % 2 != 0 and int(n[i]) % 2 == 0: return False
        sum += int(n[i])
    if not ngto(sum): return False
    return True
t = int(input().strip())
for _ in range(t):
    n = input().strip()
    if check(n): print('YES')
    else: print('NO')