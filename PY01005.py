n = input()
def check(a,b):
    s = a+b
    if s == 4 or s == 7: print('YES')
    else: print('NO')
s4 = 0
s7 = 0
for i in range(len(n)):
    if n[i] == '4': s4 += 1
    if n[i] == '7': s7 += 1
check(s4,s7)