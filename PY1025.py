s = input()
cnt = s[-3:] # lấy 3 kí tự cuối

for i in range(len(s)-3, 0, -3):
    if i - 3 > 0:  # nếu nó chưa phải kiểu 1,000,000 thì
        cnt = s[i-3:i] + ',' + cnt # lấy 3 số từ số i-3 đến i
    else:
        cnt = s[:i] + ',' + cnt

print(cnt)
