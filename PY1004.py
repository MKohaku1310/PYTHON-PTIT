import math

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def check(N):
    cnt = 0
    for i in range(1, N):
        if math.gcd(i, N) == 1:
            cnt += 1
    return "YES" if is_prime(cnt) else "NO"

t = int(input())
for _ in range(t):
    N = int(input())
    print(check(N))
