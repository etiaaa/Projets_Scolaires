tableau = []

for i in range(4):
    lignes = []
    for j in range(4):
        lignes.append(i)
    tableau.append(lignes)

print(tableau)

for lignes in tableau:
    for elem in lignes:
        print(lignes[elem])


