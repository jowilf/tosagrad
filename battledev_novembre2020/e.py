import sys

M = 4294967296
s = input()
n_i = sum([ord(c) * pow(31, i) for (i, c) in enumerate(reversed(s))]) % M
arr = []
sys.stderr.write(f"ni {n_i}\n")
rep = s
k = 0 if n_i > 33 else 1
while rep == s:
    n = n_i + M * k
    sys.stderr.write(f"new n {n}\n")
    while n > 126:
        r = n % 31
        r += 31
        if r < 33: r += 31
        n = (n - r) / 31
        arr.append(r)
    arr.append(n)
    sys.stderr.write(f"sum {sum([v * pow(31, i) for (i, v) in enumerate((arr))]) % M}\n")
    # print(arr)
    k += 1
    rep = "".join(map(lambda v: chr(int(v)), reversed(arr)))

sys.stderr.write(f"{s} <---> {rep}\n")
print(rep)
