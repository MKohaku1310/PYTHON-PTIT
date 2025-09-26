for _ in range(int(input())):
    n = int(input())
    ok = True
    a = n
    while(True):
        if a % 7 == 0:
            ok = False
            print(a)
            break
        else:
            s = int(str(a)[::-1])
            d = a + s
            if d % 7 == 0:
                ok = False
                print(d)
                break
            else: a = d
    if ok == True:
        print(-1)      
