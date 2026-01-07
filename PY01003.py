t = int(input())
for _ in range(t):
    n = int(input())
    mu = 10
    while n > mu :
        n = (n + mu // 2) // mu * mu
        mu *= 10
    print (n)