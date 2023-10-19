from Rules_Alak import *

Jouer = Alak(9)

print("Fonction Board: ", Jouer.newBoard())
Jouer.display()
print("Fonction Possible: ", Jouer.possible(2))
print("Fonction Selection: ", Jouer.select())
print("Fonction Put: ", Jouer.put())
# print("Fonction Again :", Jouer.again())
print("Fonction Captured: ", Jouer.captured())
print("Fonction Again: ", Jouer.again())
print("Fonction Win: ", Jouer.win())