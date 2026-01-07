t = int(input())

for _ in range(t):
    N = input().strip()

    tich = 1
    tong = 0
    co_so_khac_0 = False

    for i, ch in enumerate(N):
        so = int(ch)
        if i % 2 == 0:          # vị trí chẵn → tính tích
            if so != 0:
                tich *= so
                co_so_khac_0 = True
        else:                   # vị trí lẻ → tính tổng
            tong += so

    if not co_so_khac_0:
        tich = 0

    print(tich, tong)
