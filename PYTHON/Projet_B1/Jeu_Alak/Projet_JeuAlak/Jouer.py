from Rules_Alak import *

#Mise en place du jeu
Jouer = Alak(9)  # Création de l'instance du jeu

Jouer.newBoard()
Jouer.display()
for i in range(2):
    print(Jouer.put())
    Jouer.player = 2

Jouer.player = 1
while Jouer.again() != False:  # Boucle de jeu
    Jouer.player = 2
    print(Jouer.put())
    Jouer.player = 1

print(Jouer.win())
 