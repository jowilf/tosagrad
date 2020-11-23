n = int(input())
db = dict()
pdb = dict()
for i in range(n - 1):
    p, v = map(int, input().split())
    db[v] = db.get(v, 0) + 1
    pdb[v] = p
for key in db.keys():
    if db[key] == 1:
        print(pdb[key])
