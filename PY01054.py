def check(n):
    tich = 1
    for i in range(len(n)):
        if(int(n[i])!=0):
            tich *= int(n[i])
    return tich
t = int(input().strip())
for _ in range(t):
    n = input().strip()
    print(check(n))