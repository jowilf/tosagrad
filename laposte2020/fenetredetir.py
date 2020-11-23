import re

n = int(input())
pattern = r"(\d\d):(\d\d)-(\d\d):(\d\d)"
rec = re.compile(pattern)
tab = [[False for _ in range(60)] for __ in range(24)]


def fill(h1, m1, h2, m2):
    # print("fill", h1, m1, h2, m2)
    if h1 == h2:
        for m in range(m1, m2 + 1):
            tab[h1][m] = True
    else:
        for h in range(h1, h2 + 1):
            if h == h1:
                s, e = m1, 60
            elif h != h2:
                s, e = 0, 60
            else:
                s, e = 0, m2 + 1
            for m in range(s, e):
                tab[h][m] = True


cmax, out = 0, "IMPOSSIBLE"
for i in range(n):
    h1, m1, h2, m2 = map(int, rec.match(input().strip()).groups())
    # print(h1, m1, h2, m2)
    if h1 <= h2:
        fill(h1, m1, h2, m2)
    else:
        fill(h1, m1, 23, 59)
        fill(0, 0, h2, m2)
hs, ms, he, me = -1, -1, -1, -1
h, m, c = 0, 0, 0
cf, hf, mf = 0, -1, -1
interrupt = False
while h < 24:
    m = 0
    while m < 60:
        if not tab[h][m]:
            if hs == -1:
                hs, ms, he, me = h, m, h, m
            else:
                he, me = h, m
            c += 1
        else:
            if c > cmax:
                out = '{:02d}:{:02d}-{:02d}:{:02d}'.format(hs, ms, he, me)
                cmax = c
            if (hs, ms) == (0, 0):
                hf, mf = he, me
                cf = c
            hs, ms, he, me = -1, -1, -1, -1
            c = 0
        if he == 23 and me == 59 and hf != -1:
            nc = c + cf
            if nc > cmax:
                out = '{:02d}:{:02d}-{:02d}:{:02d}'.format(hs, ms, hf, mf)
        m += 1
    h += 1
print(tab[0])
print(out)
