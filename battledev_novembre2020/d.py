from math import ceil, log2


def getMid(s, e):
    return s + (e - s) // 2


def getXorUtil(st, ss, se, qs, qe, si):
    if (qs <= ss and qe >= se):
        return st[si]
    if (se < qs or ss > qe):
        return 0
    mid = getMid(ss, se)

    return getXorUtil(st, ss, mid, qs, qe, 2 * si + 1) ^ \
           getXorUtil(st, mid + 1, se, qs, qe, 2 * si + 2)


def getXor(st, n, qs, qe):
    if (qs < 0 or qe > n - 1 or qs > qe):
        return 0

    return getXorUtil(st, 0, n - 1, qs, qe, 0)


def constructSTUtil(arr, ss, se, st, si):
    if (ss == se):
        st[si] = arr[ss]
        return arr[ss]
    mid = getMid(ss, se)
    st[si] = constructSTUtil(arr, ss, mid, st, si * 2 + 1) ^ \
             constructSTUtil(arr, mid + 1, se, st, si * 2 + 2)

    return st[si]


def constructST(arr, n):
    x = (int)(ceil(log2(n)))
    max_size = 2 * (int)(2 ** x) - 1
    st = [0] * (max_size)
    constructSTUtil(arr, 0, n - 1, st, 0)
    return st


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    st = constructST(arr, n)
    ans = [0] * 256
    for i in range(m):
        l, r = map(int, input().split())
        rep = getXor(st, n, l, r)
        # print(rep)
        ans[rep] += 1
    print(" ".join(map(str, ans)))
