def check(n):
    s = str(sum(int(i) for i in n))
    return len(s) > 1 and s == s[::-1]

t = int(input().strip())
for _ in range(t):
    s = input().strip()
    if check(s):
        print('YES')
    else:
        print('NO')