import math
a,b = map(int,input().split())
for i in range(a,b-1):
    for j in range(i+1,b):
        if math.gcd(i,j) != 1:
            continue
        for c in range(j+1,b+1):
            if math.gcd(i,c) == 1 and math.gcd(j,c) == 1:
                print(f"({i}, {j}, {c})")