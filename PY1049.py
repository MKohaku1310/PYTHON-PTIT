def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def check(s):
    cnt_prime = 0
    cnt_nonprime = 0
    for c in s:
        if c in '2357':
            cnt_prime += 1
        else:
            cnt_nonprime += 1
    if is_prime(len(s)) and cnt_prime > cnt_nonprime:
        return True
    return False

for _ in range(int(input())):
    s = input().strip()
    if check(s):
        print('YES')
    else:
        print('NO')