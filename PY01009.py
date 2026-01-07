s = input()
s1 = 0
s2 = 0
for i in range(len(s)):
    if s[i] >= 'A' and s[i] <= 'Z': s2 += 1
    if s[i] >= 'a' and s[i] <= 'z': s1 += 1

if s1 >= s2 : print(s.lower())
else: print(s.upper())
