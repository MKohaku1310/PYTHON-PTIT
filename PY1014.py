a, k, n = map(int, input().split())
res = []
r = a % k
b1 = (k - r) % k 
if b1 == 0:
    b1 = k
for b in range(b1, n - a + 1, k):
    res.append(b)
if res:
    print(" ".join(map(str, res)))
else:
    print(-1)
