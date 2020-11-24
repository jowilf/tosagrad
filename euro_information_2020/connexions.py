n, m = map(int, input().split())
adjs = [set() for _ in range(n)]
for _ in range(m):
    i, j = map(lambda v: int(v) - 1, input().split())
    adjs[i].add(j)
counts = [-1] * n


def get_count(node):
    c = 1
    for child in adjs[node]:
        c += get_count(child)
    counts[node] = c
    # print(f"count {node} == {c}")
    return c

ans, c = -1, 0
for i in range(n):
    if counts[i] == -1:
        get_count(i)
    k = counts[i]
    if k > c:
        c = k
        ans = i
# print(counts)
print(ans + 1)
