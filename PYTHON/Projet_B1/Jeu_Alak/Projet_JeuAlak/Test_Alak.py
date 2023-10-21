from Rules_Alak import *

#Test de chaque fonction au cours de la programmation du jeu
Test = Alak(9)

Test.newBoard()
Test.display()
print("Fonction Possible: ", Test.possible())
print("Fonction Selection: ", Test.select())
print(Test.put())
print("Fonction Again: ", Test.again())
print("Fonction Win: ", Test.win())

