import sys

sys.setrecursionlimit(10000)
n, k = map(int, input().split())
br = input().strip()
dec = []
pdb = []#[[None for _ in range(n)] for __ in range(n)]


# sys.stderr.write(f"{n} {k}\n{br}\n")


def is_palindrome(i, j):
    if i == j: return True
    # print(br[i:j + 1], j - i + 1)
    if pdb[i][j] != None:
        # print('db')
        return pdb[i][j]
    for ii in range((j - i + 1) // 2):
        # print(br[i + ii], br[j - ii])
        if pdb[i + ii][j - ii] != None:
            pdb[i][j] = pdb[i + ii][j - ii]
            return pdb[i][j]
        if br[i + ii] != br[j - ii]:
            pdb[i][j] = False
            pdb[i + ii][j - ii] = False
            return pdb[i][j]
    pdb[i][j] = True
    return pdb[i][j]


adjs = [[] for _ in range(n)]
"""cn = 0
for i in range(n):
    for j in range(i + 1, n):
        if is_palindrome(i, j):
            adjs[i].append(j)"""
for i in range(n):
    # print(i)
    lptr, rptr = i, i
    adjs[lptr].append(rptr)
    while lptr > 0 and rptr < n - 1:
        lptr -= 1
        rptr += 1
        if br[lptr] != br[rptr]:
            break
        adjs[lptr].append(rptr)
    if i != 0 and br[i] == br[i - 1]:
        lptr, rptr = i - 1, i
        adjs[lptr].append(rptr)
        while lptr > 0 and rptr < n - 1:
            lptr -= 1
            rptr += 1
            if br[lptr] != br[rptr]:
                break
            adjs[lptr].append(rptr)

# print("stt")
visited = [[False for _ in range(k)] for __ in range(n)]


def dfs(node):
    # print(f"node {node}", visited)
    if node >= n:
        return
    if visited[node][len(dec)]:
        # print("a")
        return
    for child in adjs[node]:
        dec.append(br[node: child + 1])
        if child == n - 1 and len(dec) == k:
            print(" ".join(dec))
            exit()
        if len(dec) < k:
            dfs(child + 1)
        dec.pop()
    visited[node][len(dec)] = True


dfs(0)
print("IMPOSSIBLE")
