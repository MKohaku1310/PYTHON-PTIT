t = int(input().strip())
for _ in range(t):
    s = input().strip()

    if s[0] == s[len(s)-2] and s[1] == s[len(s)-1]: print('YES')
    else: print('NO')