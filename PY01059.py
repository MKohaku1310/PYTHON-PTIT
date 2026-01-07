t = int(input())

for _ in range(t):
    N = input().strip()

    tong = 0
    tich = 1
    co_so_khac_0 = False

    for i, ch in enumerate(N):
        so = int(ch)
        if i % 2 == 0:          # vị trí chẵn
            tong += so
        else:                   # vị trí lẻ
            if so != 0:
                tich *= so
                co_so_khac_0 = True

    if not co_so_khac_0:
        tich = 0

    print(tong, tich)
