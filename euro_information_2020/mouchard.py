COLORS = """!"#$%&'()*+,-./:;<=>?@[]\\^_`{|}~"""
n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]


def is_possible(r, c):
    return 0 <= r < n and 0 <= c < m


def is_valid42(r, c, rp, cp):
    if not is_possible(rp, cp): return False
    for i in range(r, rp + 1):
        for j in range(c, cp + 1):
            if grid[i][j] != grid[r][c]:
                return False
            for (dx, dy) in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                rr, cc = i + dx, j + dy
                if is_possible(rr, cc) and grid[rr][cc] == grid[r][c] and not (r <= rr <= rp and c <= cc <= cp):
                    return False
    return True


tab = []
for i in range(n):
    for j in range(m):
        if grid[i][j] in COLORS and (is_valid42(i, j, i + 3, j + 1) or is_valid42(i, j, i + 1, j + 3)):
            tab.append((i + 1, j + 1))
print(len(tab))
for i, j in tab:
    print(i, j)
