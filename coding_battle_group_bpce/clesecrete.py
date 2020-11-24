import sys

sys.setrecursionlimit(10000)
input()
source = input().strip()
target = input().strip()
best = source
bdiff = float("inf")


def diff(s, t):
    i = 0
    for j in range(len(s)):
        if s[j] != t[j]: i += 1
    return i


fringe = set()


def left_shift(s):
    return s[1:] + s[0]


def increment(s):
    res = []
    for l in s:
        i = ord(l) - ord('a') + 1
        i %= 26
        res.append(chr(97 + i))
    return "".join(res)


def search(s):
    global bdiff, target, best
    # print(fringe)
    fringe.add(s)
    _d = diff(s, target)
    if _d < bdiff:
        bdiff = _d
        best = s
        # print(best)
    transformed = [increment(s), left_shift(s)]
    for word in transformed:
        if word not in fringe:
            search(word)


search(source)
print(best)
