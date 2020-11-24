tab = [0] * 50001
c, ans = 0, -1
for _ in range(int(input())):
    n = int(input())
    tab[n] += 1
    if tab[n] > c:
        ans = n
        c = tab[n]
print(ans)
