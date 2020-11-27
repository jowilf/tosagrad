import sys

M = 4294967296
s = input()
#Calcul du hash
hash = sum([ord(c) * pow(31, i) for (i, c) in enumerate(reversed(s))]) % M
sys.stderr.write(f"ni {hash}\n")
ans = s
k = 0 if hash > 33 else 1
"""
L'idée ici est de pouvoir décomposer la valeur du hash comme si on devrait écrit la valeur du hash
dans la base 31 (https://fr.wikipedia.org/wiki/Base_(arithm%C3%A9tique). Mais si on décompose comme on n'a l'habitude de le faire, tous les coefficients seront 
inferieurs à 31 or les coefficients doivent être compris entre 33 et 126. Nous devons donc faire en sorte
que les restes soient compris entre 33 et 126. Pour cela on ajoute 31 au reste après chaque division.
Dans le cas où il y a collision avec le le pseudonyme du chef de réseau on ajoute la valeur 4294967296 (on peut se le permettre à cause du modulo)
puis on recommence le calcul (le second calcul sera forcément différent du pseudonyme).
"""
while ans == s:
    n = hash + M * k
    arr = []
    sys.stderr.write(f"new n {n}\n")
    while n > 126:
        r = n % 31
        # On ajoute 31 pour que r puisse rester dans l'intervalle 33 à 126
        r += 31
        # Dans le cas ou r < 2 il faut ajouter encore 31
        if r < 33: r += 31
        n = (n - r) / 31
        arr.append(r)
    # On ajoute le reste
    arr.append(n)
    sys.stderr.write(f"sum {sum([v * pow(31, i) for (i, v) in enumerate((arr))]) % M}\n")
    # print(arr)
    k += 1
    ans = "".join(map(lambda v: chr(int(v)), reversed(arr)))

sys.stderr.write(f"{s} <---> {ans}\n")
print(ans)
