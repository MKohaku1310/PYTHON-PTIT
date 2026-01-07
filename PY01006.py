t=int(input().strip())
while t>0:
    n=int(input().strip())
    s=0
    while n>0:
        m=n%10
        if m!=4 and m!=7:
            s+=1
        n//=10
    if s==0: print('YES')
    else: print('NO')
    t-=1
