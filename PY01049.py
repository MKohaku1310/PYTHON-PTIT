def ngto(n):
    if n < 2: return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: return False
    return n > 1
def check(n):
    sngt = 0
    stn = 0
    for ch in n:
        if ch in '2357': sngt += 1
        else: stn += 1
    if sngt > stn: return True
    else: return False
t = int(input().strip())
for _ in range(t):
    s = input().strip()
    if ngto(len(s)) and check(s): print('YES')
    else: print('NO')  