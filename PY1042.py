def check(s):
    for i in range(len(s)):
        if s[i] not in '012': return 0
    return 1

for t in range(int(input())):
    s = input()
    if check(s): print('YES')
    else : print('NO')
