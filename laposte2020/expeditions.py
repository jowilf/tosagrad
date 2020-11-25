tab = []
vdb = dict()
for _ in range(int(input())):
    c, v = input().split()
    vdb[c] = int(v)
    tab.append(c)
set1, set2 = set(), set()
dmin = float("inf")
s1, s2 = [], []


def sumset(s):
    return sum(map(lambda k: vdb[k], s))


def search(i):
    global dmin, set1, set2, tab, s1, s2
    if len(set1) + len(set2) == len(tab):
        d = abs(sumset(set1) - sumset(set2))
        if d < dmin:
            dmin = d
            s1, s2 = list(set1), list(set2)
        return
    set1.add(tab[i])
    search(i + 1)
    set1.remove(tab[i])
    set2.add(tab[i])
    search(i + 1)
    set2.remove(tab[i])


search(0)
print(" ".join(s1))
print(" ".join(s2))
