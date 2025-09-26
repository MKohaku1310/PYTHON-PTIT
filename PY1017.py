t = int(input())
for _ in range(t):
    s = input().strip()
    res=""
    i = 0
    while i<len(s):
        cnt = 1
        while i+1<len(s) and s[i]==s[i+1]:
            cnt +=1
            i+=1
        res += str(cnt)+s[i]
        i+=1
    print(res)