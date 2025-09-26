def nto(n):
    if n < 2: return False
    for i in range(2,n//2,1):
        if n % i == 0: return False
    return True

def check(n):
    sum = 0
    for c in n:
        sum += int(c)
    if nto(sum): return True
    return False
t = int(input())
for _ in range(t):
    s = input()
    if check(s): print("YES")
    else : print("NO")