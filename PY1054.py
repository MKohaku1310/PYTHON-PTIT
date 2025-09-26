def tong(s):
    sum = 1
    for c in s:
        if c != '0':
            sum *= int(c)
    return sum
t = int(input())
for _ in range(t):
    n = input()
    print(tong(n))