def tong(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum % 3 == 0
t = int(input().strip())
for _ in range(t): 
    n = input().strip()
    if tong(n): print('YES')
    else: print('NO')