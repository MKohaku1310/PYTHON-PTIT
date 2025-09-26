def check(s):
    # Kiểm tra chỉ có 2 chữ số khác nhau
    if len(set(s)) != 2:
        return 0
    # Kiểm tra các chữ số cách nhau 2 vị trí đều bằng nhau
    for i in range(len(s) - 2):
        if s[i] != s[i+2]:
            return 0
    return 1

for t in range(int(input())):
    s = input().strip()
    if check(s):
        print('YES')
    else:
        print('NO')