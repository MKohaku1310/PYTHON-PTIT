p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.' #tạo 1 chuỗi gồm 28 kí tự
def int(x):
    return p.index(x) #ham trả về vị trí của ký tự x trong chuỗi p
while 1: 
    s = input()
    if(s[0]=='0'):
        break; #vòng lặp vô hạn chỉ dừng khi chuỗi bắt đầu bằng số 0
    k,s = s.split() #tách số k và chuỗi s
    ans = [p[(int(x)+int(k))%28] for x in s] #Với mỗi ký tự x trong chuỗi s: Tìm vị trí của x trong bảng p.Cộng thêm k (số nguyên), sau đó lấy phần dư cho 28 (để quay vòng bảng chữ cái).Lấy ký tự mới từ bảng p theo vị trí vừa tính.
    print(''.join(reversed(ans)))

