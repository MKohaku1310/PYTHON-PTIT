def nto(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def check(n):
    # check các vị trí chẵn (0,2,4,...) phải là số lẻ
    for i in range(0, len(n), 2):
        if int(n[i]) % 2 != 0:
            return False

    # check các vị trí lẻ (1,3,5,...) phải là số chẵn
    for i in range(1, len(n), 2):
        if int(n[i]) % 2 == 0:
            return False

    # check tổng chữ số là số nguyên tố
    s = sum(int(c) for c in n)
    if not nto(s):
        return False

    return True


t = int(input())
for _ in range(t):
    n = input().strip()
    print("YES" if check(n) else "NO")
