class Alak:
    
    def __init__(self): 
        self.n = 0  # Attribut pour la longueur du plateau
        self.board = []  # Attribut qui représente le plateau du jeu 
        self.player = range(1,2)
        self.removed = []  # Attribut qui représente le plateau du jeu 
        self.i = 0

    
    def newBoard(self, n):  # Fonction newBoard avec un paramètre n
        self.n = n  # Assigner n à l'attribut self.n
        self.board = []  # Réinitialiser le plateau
        for i in range(1,n+1):  # Initialisation de la taille du plateau en fonction de l'argument n
            self.board.append(i)
        return self.board  # On retourne le tableau


    def display(self,board,n): #Fonction display qui permet l'affichage de la fonction du jeu
        self.case = range(3)
        for i in range(n):
            if self.case == 1:            
                board[i] = "x"
            elif self.case == 2:
                board[i] = "o"
            else:
                board[i] = "."
        return str(board) + "\n" + str([1,2,3,4,5,6,7,8,9])


    def possible(board,n,player,removed,i):

        if i < 0 or i >= n:
            return False

        for case in board:
            #Pour joueur 1
            if player == 1:
                if i == ".":
                    return True

            
            #Pour joueur 2
            if player == 2:
                if i == ".":
                    return True
        return False


Jouer = Alak()
# Board = Jouer.newBoard(9)
# print(Board)

Display = Jouer.display([1,2,3,4,5,6,7,8,9],9)
print(Display)

# Possible = Jouer.possible(self.board,9,1,None,4)
# print(Possible)