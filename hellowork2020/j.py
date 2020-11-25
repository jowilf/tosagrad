def GetPalindromeList(s):
    pals = []
    for i in range(len(s)):
        print(i)
        lptr, rptr = i, i
        pals.append((i, 1))
        while lptr > 0 and rptr < len(s) - 1:
            lptr -= 1
            rptr += 1
            if s[lptr] != s[rptr]:
                break
            pals.append((lptr, rptr - lptr + 1))
        if i != 0 and s[i] == s[i - 1]:
            lptr, rptr = i - 1, i
            pals.append((lptr, 2))
            while lptr > 0 and rptr < len(s) - 1:
                lptr -= 1
                rptr += 1
                if s[lptr] != s[rptr]:
                    break
                pals.append((lptr, rptr - lptr + 1))
    return sorted(pals)


def solve(s, nsplit=None):
    pals = GetPalindromeList(s)
    dpMax = nsplit or 500
    dp = [{} for _ in range(len(s) + 1)]
    dp[0][0] = 0
    for pal in pals:
        for k in dp[pal[0]]:
            if k < dpMax:
                dp[pal[0] + pal[1]][k + 1] = pal[1]
    if nsplit is None:
        return min(dp[-1], default=None)
    if nsplit not in dp[-1]:
        return None
    ls = []
    ptr = len(s)
    for k in range(nsplit, 0, -1):
        ls.append(dp[ptr][k])
        ptr -= dp[ptr][k]
    ptr = 0
    result = []
    for ln in ls[::-1]:
        result.append(s[ptr:ptr + ln])
        ptr += ln
    return ' '.join(result)


n, k = map(int, input().split())
print(solve(input(), k) or 'IMPOSSIBLE')

