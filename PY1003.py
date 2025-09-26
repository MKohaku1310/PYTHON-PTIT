t = int(input())
for _ in range(t):
    n = int(input())
    mul = 10
    while n >= mul:
        # Làm tròn lên nếu phần dư >= 5 * (mul // 10)
        if n % mul >= mul // 2:
            n = n + (mul - n % mul)
        else:
            n = n - (n % mul)
        mul *= 10
    print(n)