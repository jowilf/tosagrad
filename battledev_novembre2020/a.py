r = 0
for i in range(int(input())):
    s = input().strip()
    ans = True
    # print(s[-5:])
    for c in s[-5:]:
        if not c.isdigit():
            ans = False
    if ans:
        r += 1
print(r)
