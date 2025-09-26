s = input().strip() # đọc chuỗi s
chu_thuong = sum(1 for ch in s if ch.islower())
chu_hoa = sum(1 for ch in s if ch.isupper())
if chu_thuong >= chu_hoa:
    print(s.lower())
else:
    print(s.upper())