from random import *
from numpy import *
import pyautogui
import time  

class JustGetTen:

    def __init__(self):
        self.grid = [] #On initialise la grille vide
        self.newGrid()

    def newGrid(self): 
        """
        Fonction qui as pour but d'initialiser la taille de la grille en fonction du choix du joueur
        """
        self.choice_grid = int(input("Please, choose a number between 1 and 5 for the size of your game grid: "))
        #La ligne ci-dessus demande au joueur de choisir entre 5 choix de grilles (de la plus petite à la plus grande taille)
        
        while self.choice_grid < 1 or self.choice_grid > 5:
            print("I'm sorry, the number choose is not between 1 and 5, please restart")        
            self.choice_grid = int(input("Please, choose a number between 1 and 5 for the size of your game grid: "))
        if self.choice_grid == 1: #Pour le choix 1 la taille de la grille est de 4 lignes et 4 colonnes
            print("Well you choose the number 1, the size of your grid of game is 4x4 :")
            for ligne in range(4): #On procède donc à la création de grille
                lignes = []  # Créez une sous-liste vide pour chaque ligne
                for colonne in range(4):
                    lignes.append(random.choice([1, 2, 3, 4], p=[0.4, 0.3, 0.25, 0.05])) 
                    #La ligne ci-dessus permet de définir a une case qui vaut entre 1 et 4 avec les probabilités définit
                self.grid.append(lignes)
            return self.grid 
        
        #On fais de même pour la suite, pour le choix 2 la taile de la grille est de 5 lignes et 5 colonnes        
        elif self.choice_grid == 2:
            print("Well you choose the number 2, the size of your grid of game is 5x5 :")
            for ligne in range(5):
                lignes = []  # Créez une sous-liste vide pour chaque ligne
                for colonne in range(5):
                    lignes.append(random.choice([1, 2, 3, 4], p=[0.4, 0.3, 0.25, 0.05])) 
                    #La ligne ci-dessus permet de définir a une case qui vaut entre 1 et 4 avec les probabilités définit
                self.grid.append(lignes)
            return self.grid   
        
        #Pour le choix 3 la taille de la grille est de 6 lignes et 6 colonnes
        elif self.choice_grid == 3:
            print("Well you choose the number 3, the size of your grid of game is 6x6 :")
            for ligne in range(6):
                lignes = []  # Créez une sous-liste vide pour chaque ligne
                for colonne in range(6):
                    lignes.append(random.choice([1, 2, 3, 4], p=[0.4, 0.3, 0.25, 0.05])) 
                    #La ligne ci-dessus permet de définir a une case qui vaut entre 1 et 4 avec les probabilités définit
                self.grid.append(lignes)
            return self.grid   

        #Pour le choix 4 la taille de la grille est de 7 lignes et 7 colonnes            
        elif self.choice_grid == 4:
            print("Well you choose the number 4, the size of your grid of game is 7x7 :")
            for ligne in range(7):
                lignes = []  # Créez une sous-liste vide pour chaque ligne
                for colonne in range(7):
                    lignes.append(random.choice([1, 2, 3, 4], p=[0.4, 0.3, 0.25, 0.05])) 
                    #La ligne ci-dessus permet de définir a une case qui vaut entre 1 et 4 avec les probabilités définit
                self.grid.append(lignes)
            return self.grid        

        #Pour le choix 5 la taille de la grille est de 8 lignes et 8 colonnes
        elif self.choice_grid == 5:
            print("Well you choose the number 5, the size of your grid of game is 8x8 :")
            for ligne in range(8):
                lignes = []  # Créez une sous-liste vide pour chaque ligne
                for colonne in range(8):
                    lignes.append(random.choice([1, 2, 3, 4], p=[0.4, 0.3, 0.25, 0.05])) 
                    #La ligne ci-dessus permet de définir a une case qui vaut entre 1 et 4 avec les probabilités définit
                self.grid.append(lignes)
            return self.grid
    

    def displayGrid(self): 
        """
        Fonction qui permet d'afficher la Grille de jeu
        """
        JustGetTen.newGrid(self) #On utilise la fonction qui as généré la Grille c.a.d newBoard
        horizontal_line = "+ " + "-" * (4 * len(self.grid[0]) -3) + " +" #On définit les traits qui marqueront la séparation des éléments de la grille
        print(horizontal_line) #On affiche la ligne de démarcation sur le haut du tableau
        for ligne in self.grid: #On affiche les différentes lignes de la grille
            for case in ligne: #Pour chaque case sur une ligne
                print(f"| {case} ", end="") #On sépare les cases par des traits
            print("|") #On ajoute une ligne de démarcation sur le bas du tableau
            print(horizontal_line) #On l'affiche


    def MouseContact(self):
        """
        Fonction qui permet de séléctionner les cases grâce à la souris
        """
        for case in self.grid:
            None

        time.sleep(2)
        # Obtenez les coordonnées actuelles de la souris
        x, y = pyautogui.position()
        print(f"Position actuelle de la souris : ({x}, {y})")
        # Effectuez un clic de souris en utilisant les coordonnées obtenues
        pyautogui.click(x, y, button='left')
        # # Effectuez un double-clic de souris
        # pyautogui.doubleClick(x, y)
        # # Effectuez un clic droit de souris
        # pyautogui.click(x, y, button='right')

    def StateCase(self): 
        """
        Fonction qui permet de vérifier l'état des cases adjacentes d'une case choisi
        """
        self.select_case = int(input("Please select a number to Ge:"))
        #La ligne ci-dessus demande au joueur de choisir une case à séléctionner pour commencer les règles de fusion
        # total = 0
        # for ligne in self.grid:
        #     for case in self.grid:
        #         None
        None
                 

    def MergeCase(self):
        """
        Fonction qui permet de fusionner les cases de même valeur
        """
        None

    
    def FallCase(self):
        """
        Fonction qui permet de remplacer et générer de nouvelles cases
        """
        None
    

    def UpdateGrid(self):
        """
        Fonction qui met à jour la grille du jeu
        """
        None


    def UserScore(self):
        """
        Fonction qui informe le joueur de son score actuelle
        """
        None


    def Again(self):
        """
        Fonction qui en cas d'échec affiche les score du joueur 
        et ainsi lui propose de rejouer
        """
        None



#Session Test:

Test = JustGetTen()

# print(Test.newGrid())
Test.displayGrid()
Test.MouseContact()