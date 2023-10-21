from Rules_Alak import *

#Mise en place du jeu
Jouer = Alak(9)  # Création de l'instance du jeu
Jouer.newBoard()
Jouer.display()

while Jouer.again() == True:  # Boucle de jeu
    Jouer.put()
    Jouer.player = 3 - Jouer.player  # Permet de basculer entre les joueurs 1 et 2
print(Jouer.win())
 