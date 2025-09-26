def count_risk_cases(matrix):
    M = len(matrix)
    N = len(matrix[0])

    # 8 hướng xung quanh một ô
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    total_risk = 0

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == -1:
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < M and 0 <= nj < N and matrix[ni][nj] >= 0:
                        total_risk += 1
    return total_risk


# Nhập kích thước ma trận
M, N = map(int, input().split())

# Nhập ma trận
matrix = []
for _ in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

# In kết quả
print(count_risk_cases(matrix))