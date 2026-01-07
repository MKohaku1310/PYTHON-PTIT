t = int(input().strip())
for _ in range(t):
    s = input().strip()
    sum = 0
    ok = True
    for i in range(len(s)):
        sum += int(s[i])
    if sum % 10 != 0:
        ok = False
    else :
        for i in range(len(s)-1):
            if abs(int(s[i])-int(s[i+1])) != 2:
                ok = False
                break
    if ok: print("YES")
    else: print('NO')
