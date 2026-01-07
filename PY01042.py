def check(s):
    for ch in s:
        if ch not in "012":
            return False
    return True
t = int(input().strip())

for _ in range(t):
    s = input().strip()
    if check(s): print('YES')
    else : print('NO')