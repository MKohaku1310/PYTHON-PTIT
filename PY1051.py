for t in range(int(input())):  # chạy test
    def dao(s):
        if len(s) <= 1:
            return 'NO'
        return 'YES' if s == ''.join(reversed(s)) else 'NO'

    def tcs(n):  # tính tổng chữ số
        tong = 0
        for i in n:
            tong += int(i)
        return dao(str(tong))  # kiểm tra tổng đó có phải số thuận nghịch không

    print(tcs(input()))
