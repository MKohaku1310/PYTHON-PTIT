t = int(input().strip())

for _ in range(t):
    s = input().strip()
    res = ""
    i = 0
    while i< len(s):
        ch = s[i]
        cnt = int(s[i+1])
        res += ch*cnt
        i+=2
    print(res)