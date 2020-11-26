c = 0
n = int(input())
for i in range(n):
    h, m = map(int,input().split(":"))
    if h >= 20 or h < 8:
        c += 1
print("SUSPICIOUS" if c > (n / 2) else "OK")
