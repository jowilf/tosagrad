s, p = -1, ""
for _ in range(int(input())):
    ss, pp = input().split()
    ss = int(ss)
    if ss > s:
        s = ss
        p = pp
print(p)
