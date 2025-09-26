t=int(input().strip()) # đọc số nguyên t
for _ in range(t):
    n = input().strip() # đọc chuỗi n
    if all(ch in '47' for ch in n): # kiểm tra xem tất cả ký tự trong n có phải là '4' hoặc '7' không
        print('YES')
    else:
        print('NO')