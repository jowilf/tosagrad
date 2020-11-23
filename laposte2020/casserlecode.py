n = int(input())
msg = input().strip()
l = len(msg) // n
code = ""
for i in range(n):
    for j in range(l):
        code += msg[n * j + i]
        #print('-->', i, j, n * j + i, msg[n * j + i])
print(code)
# RFsarAbi1Dt4eeh
# RabDeFritesA14h
