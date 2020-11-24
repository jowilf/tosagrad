import re, sys

int_val = lambda h, m: M * h + m
s_val = lambda hm: (hm // M, hm - (hm // M) * M)
n = int(input())
pattern = r"(\d\d):(\d\d)-(\d\d):(\d\d)"
rec = re.compile(pattern)
H, M = 24, 60
tab = [False] * (H * M)
for i in range(n):
    h1, m1, h2, m2 = map(int, rec.match(input().strip()).groups())
    hm1, hm2 = int_val(h1, m1), int_val(h2, m2)
    # print(hm1, hm2)
    if hm1 <= hm2:
        for hm in range(hm1, hm2 + 1): tab[hm] = True
    else:
        for hm in range(hm1, H * M): tab[hm] = True
        for hm in range(0, hm2 + 1): tab[hm] = True
if all(tab):
    print("IMPOSSIBLE")
elif not any(tab):
    print("00:00-23:59")
else:
    hm, cmax, hms, hme, c = 0, 0, -1, -1, 0
    bhms, bhme = -1, -1
    hm0e = -1
    while hm < H * M:
        if not tab[hm]:
            if hms == -1: hms = hm
            hme = hm
            c += 1
        else:
            if hms == 0:
                hm0e = hme
            if c > cmax:
                cmax = c
                bhms, bhme = hms, hme
            c = 0
            hms, hme = -1, -1
        if hm == H * M - 1:
            if c > cmax:
                cmax = c
                bhms, bhme = hms, hme
            if hm0e != -1 and (hm0e + c + 1) > cmax:
                bhms, bhme = hms, hm0e
        hm += 1
    (h1, m1), (h2, m2) = s_val(bhms), s_val(bhme)
    print('{:02d}:{:02d}-{:02d}:{:02d}'.format(h1, m1, h2, m2))
