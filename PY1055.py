def check(n):
    if len(n) % 2 == 0: return False
    if n[0]==n[1]: return False
    so_dau = n[0]
    for i in range(0,len(n),2):
        if n[i]!=so_dau:
            return False
    return True
t = int(input())
for _ in range(t):
    n = input()
    if check(n): print("YES")
    else : print("NO")