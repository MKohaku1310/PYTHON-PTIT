def check(n):
    for i in range(len(n)-1):
        if int(n[i])>int(n[i+1]): return False
    return True
t = int(input().strip())
for _ in range(t):
    n = input().strip()
    if check(n): print('YES')
    else: print('NO')