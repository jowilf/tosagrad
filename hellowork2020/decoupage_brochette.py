import sys

sys.setrecursionlimit(10000)
n, k = map(int, input().split())
br = input().strip()
dec = []
pdb = [[None for _ in range(n)] for __ in range(n)]


# sys.stderr.write(f"{n} {k}\n")

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


def search(i, j):
    print(f"search {i}, {j}")
    print(dec)
    if len(dec) > k:
        return
    if j == n - 1 and not is_palindrome(i, j):
        # print(len(dec))
        # print(dec)
        return
    elif j == n - 1 and len(dec) == k - 1:
        dec.append(br[i:j + 1])
        print(" ".join(dec))
        exit()
    if j >= n: return
    if is_palindrome(i, j):
        dec.append(br[i:j + 1])
        search(j + 1, j + 1)
        dec.pop()
    search(i, j + 1)


search(0, 0)
print("IMPOSSIBLE")
