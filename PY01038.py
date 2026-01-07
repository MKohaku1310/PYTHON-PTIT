
def reverse_number(n):
    return int(str(n)[::-1])

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())

    if n % 7 == 0:
        print(n)
        continue

    found = False
    for _ in range(1000):
        n += reverse_number(n)
        if n % 7 == 0:
            print(n)
            found = True
            break

    if not found:
        print(-1)
