
def is_tang_giam(s: str) -> bool:
    # Cần tối thiểu 3 chữ số
    if len(s) < 3:
        return False

    # Chuyển thành mảng số
    a = [int(c) for c in s]

    # Bước 1: leo dốc (tăng chặt)
    i = 0
    while i + 1 < len(a) and a[i] < a[i + 1]:
        i += 1

    # Đỉnh không được ở đầu hoặc cuối
    if i == 0 or i == len(a) - 1:
        return False

    # Bước 2: xuống dốc (giảm chặt)
    while i + 1 < len(a) and a[i] > a[i + 1]:
        i += 1

    # Nếu đi hết mảng với giảm chặt thì hợp lệ
    return i == len(a) - 1


# ====== Chương trình chính ======
t = int(input().strip())
for _ in range(t):
    s = input().strip()  # đọc số dạng chuỗi, tránh vấn đề số lớn
    print("YES" if is_tang_giam(s) else "NO")
