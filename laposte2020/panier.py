total = 495
for _ in range(int(input())):
    n, p, m = map(int, input().strip().split())
    total += n * p + (125 * n * (m / 1000))
print(int(total))
