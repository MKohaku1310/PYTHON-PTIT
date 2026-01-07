def check(n):
    s = str(n)
    for i in range(len(s)-2):
        if s[i] == s[i+1] or s[i] != s[i+2]:
            return False
            break
    return True
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    if check(n): print('YES')
    else : print('NO')