n = int(input())
adjs = dict()
nivo = [None] * n
for i in range(n-1):
    a, b = map(int, input().split())
    adjs[a] = b
nivo[0] = 1


def get_nivo(i):
    if nivo[i] is None:
        return get_nivo(adjs[i]) + 1
    return nivo[i]


def run(i):
    if nivo[adjs[i]] == None:
        nivo[adjs[i]] = nivo[i] + 1
        run(adjs[i])


counts = [0] * 10
for i in range(n):
    if nivo[i] is None:
        nivo[i] = get_nivo(i)
    counts[nivo[i] - 1] += 1
print(" ".join(map(str,counts)))
