for t in range(int(input())):
    def check(s1):
        s2 =''.join(reversed(s1))
        for i in range(1,len(s1)):
            if abs(ord(s1[i])-ord(s1[i-1])) != abs (ord(s2[i])-ord(s2[i-1])): return 'NO' # ord tra ve ma ASCII
        return 'YES'
    print(check(input()))