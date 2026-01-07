a,k,n=map(int,input().split())
s=0
r=a%k
if r==0:
    b=k
if r!=0:
    b=k-r
if (k-r)>(n-a):
    print ("-1")
else:
    res=[]
    while (b<=(n-a)):
        res.append(b)
        b+=k
    print (*res)

    