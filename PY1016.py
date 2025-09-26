t = int(input())
for _ in range(t):
    s=input().strip() #doc chuoi
    res =""
    i = 0
    while(i<len(s)):
        ch = s[i]
        num =int(s[i+1])
        res += ch*num
        i += 2
    print(res)