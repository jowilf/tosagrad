N, M, a = map(int, input().split())
adjs = [set() for _ in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    adjs[i].add(j)
    adjs[j].add(i)
couts = dict()


def dfs(node, c=0):
    couts[node] = min(couts.get(node, float("inf")), c)
    for child in adjs[node]:
        if c + 1 < couts.get(child, float("inf")):
            dfs(child, c + 1)


dfs(a - 1)
m = max(couts.values())
tab = [k for k in couts.keys() if couts[k] == m]
print(" ".join(map(lambda v: str(v + 1), sorted(tab))))
