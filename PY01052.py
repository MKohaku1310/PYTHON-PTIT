def ngto(n):
    if n < 2: return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: return False
    return n > 1
def tong(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum
t = int(input().strip())
for _ in range(t):
    n = input().strip()
    d = tong(n)
    if ngto(d): print('YES')
    else: print('NO')