P = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.")
while True:
    inp = input()
    if inp == "0":
        break
    k, s = inp.split()
    k = int(k)
    res = ""
    for i in range(len(s)):
        idx = P.index(s[i])
        res += P[(idx + k) % 28]
    print(res[::-1])