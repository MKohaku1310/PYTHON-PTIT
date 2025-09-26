def check(n):
    sum = 0
    for c in n:
        sum += int(c)
    if sum % 3 == 0 : return True
    else : return False
t = int(input())
for _ in range(t):
    n = input()
    if check(n): print("YES")
    else : print("NO")