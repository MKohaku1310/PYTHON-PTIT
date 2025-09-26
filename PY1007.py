t = int(input())  # số test
for _ in range(t):
    N, X, M = map(float, input().split()) #Tóm lại: map = áp dụng hàm cho từng phần tử trong dãy. chyển đổi trạng thái
    years = 0
    while N < M:
        N *= (1 + X / 100.0)
        years += 1
    print(years)
# n*(1+x/100) >= m