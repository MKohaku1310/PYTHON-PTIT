t = int(input())

for _ in range(t):
    n,x,m = map(float, input().split())
    q = 1 + x/100
    a = 1
    while q**a<(m/n):
        a += 1
    print(a)