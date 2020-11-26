M = 4294967296
s = input()
ht = [ord(c) for c in s]
i, r, n = 0, 0, len(ht) - 1
cont = True
n = sum([ord(c) * pow(31, i) for (i, c) in enumerate(reversed(s))]) % M
arr = []
print(n)
while n > 31:
    r = n % 31
    r += 31
    if r < 33: r += 31
    n = (n - r) / 31
    arr.append(r)
print(sum([v * pow(31, i) for (i, v) in enumerate((arr))]))
print(arr)
print("".join(map(lambda v: chr(int(v)), reversed(arr))))
