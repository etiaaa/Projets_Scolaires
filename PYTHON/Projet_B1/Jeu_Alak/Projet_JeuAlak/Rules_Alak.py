class Alak:
    
    def __init__(self,n): 
        self.board = []  # Attribut qui représente le plateau du jeu 
        self.n = n  # Attribut pour la longueur du plateau
        self.player = range(1,3) #player ayant deux valeurs possibles 1 pour joueur 1 ou 2 pour joueur 2
        self.removed = []  # Attribut qui représente le plateau du jeu 
        self.empty_case = "." #Représente une case vide
        self.p1_case = "x" #Représente une case occupée par le joueur 1
        self.p2_case = "o" #Représente une case occupée par le joueur 2

    def newBoard(self):
        """        
        Fonction représentant l'état initial du plateau de jeu, c'est-à-dire plateau vide 
        actuellement représenté par "."
        """
        self.board = []  # Réinitialiser le plateau
        for i in range(self.n):  # Initialisation de la taille du plateau en fonction de l'argument n
            self.board.append(self.empty_case)
        return self.board  # On retourne le tableau


    def display(self): #Fonction display qui permet l'affichage de la fonction du jeu
        """
        Fonction d'affichage du plateau du jeu.
        """
        for case in self.board:
            if self.player == 1:
                case = self.p1_case
            elif self.player == 2:
                case = self.p2_case
            else:
                case = self.empty_case
        print(Alak.newBoard(self)) 


    def possible(self,i):
        """
        Fonction permettant de déterminer si OUI ou NON il est possible de jouer
        sur une case choisi (ici "i").
        """
        for case in self.board: 
            if case == self.empty_case:
                return True
        return False

    
    def select(self):
        """
        Fonction permettant au joueur d'indiquer la case sur laquelle il souhaite
        jouer. S'il est impossible d'y joueur alors on lui demande de choisir une autre case
        sinon la case séléctionner est valide.
        """
        self.user_choice = int(input("Choose a number to put your pawn: "))
        for case in self.board:
            while Alak.possible(self,self.user_choice) != True:
                self.user_choice = int(input("Sorry you can't choose this place, please choose a other number to put your pawn: "))
        return "Well, you choosed the number " + str(self.user_choice)


    def put(self):
        """
        Fonction qui permet de poser le pion sur la case séléctionné
        """
        Alak.select(self) 
        i = self.user_choice
        if self.player == 1:
            self.board[i] = "x"
            return self.board
        else:
            self.board[i] = "o"
            return self.board
        return "Impossibe de poser un pion"


    def captured(self):
        i = self.user_choice
        for case in self.board:
            if self.player == 1:
                if i-2 == self.p1_case and i-1 == self.p2_case:
                    self.removed.append(i-1) 
            if self.player == 2:
                if i-2 == self.p2_case and i-1 == self.p1_case:
                    self.removed.append(i-1)
                self.removed.remove(i-1)
        return "Liste des éléments supprimées" + str(self.removed) + "." +"\n Voici le nouveau plateau" + str(self.board)


    def again(self):
        for case in self.board:
            if case == self.empty_case :
                return True
        return False


    def win(self):
        p1 = []
        p2 = [] 
        for case in self.board:
            if case == self.p1_case:
                p1 += 1
            else:
                p2 +=1
        if p1 > p2:
            return "Winner: Player 1 \n Looser: Player 2"
        else:
            return "Winner: Player 2 \n Looser: Player 1"