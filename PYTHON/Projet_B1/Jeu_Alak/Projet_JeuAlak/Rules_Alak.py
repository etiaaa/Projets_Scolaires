class Alak:
    
    def __init__(self,n): 
        self.board = []  #Liste représentant le plateau du jeu 
        self.n = n  #Variable représentant la longueur n du plateau
        self.player = 1 #Représente le joueur qui joue (donc au départ, joueur 1)
        self.removed = []  #Liste représentant les pions capturés au tour précédent 
        self.empty_case = "." #Variable représentant une case vide
        self.p1_case = "x" #Variable représentant une case occupée par le joueur 1
        self.p2_case = "o" #Variable représentant une case occupée par le joueur 2


    def newBoard(self):
        """        
        Fonction représentant l'état initial du plateau de jeu, c'est-à-dire plateau vide 
        actuellement représenté par "."
        """
        self.board = []  #Réinitialisation du plateau du jeu
        for i in range(self.n):  #Initialisation de la taille du plateau en fonction de n
            self.board.append(self.empty_case) #Ajout des cases vides 


    def display(self):  
        """
        Fonction display qui permet l'affichage de la fonction du jeu
        """
        separator = "+---" * self.n + "+" #Mise en place de séparateur pour un meilleur visuel du jeu
        line_display = "| " + " | ".join(self.board) + " |" #Ligne représentant les éléments du plateau du jeu
        line_indice = "| " + " | ".join(map(str, range(self.n))) + " |" #Ligne représentant les indices des éléments du plateau du jeu

        #On affiche le tableau dans la console du jeu
        print(separator) 
        print(line_display)
        print(separator)
        print(line_indice)
        print(separator)


    def captured(self):
        """
        Fonction qui si les deux pions d'un même joueur encercle le pion du joueur 
        adverse, alors le pion adverse est capturé et le joueur ne pourra pas 
        rejouer sur la case où son pion as été capturé au tour précédent
        """
        if self.player == 1: #Pour le joueur 1
            if self.board[self.user_choice-2] == self.p1_case and self.board[self.user_choice-1] == self.p2_case:
                #Si les pions du joueur 1 encercle les pions du joueur 2
                self.removed.append(self.board[self.user_choice-1]) #Alors on capture le pion du joueur 2 en l'ajoutant a la liste des pions capturés
                self.board[self.user_choice-1] = self.empty_case #Et en le supprimant du plateau du jeu
                return True #Si la condition est vrai on renvoie vrai pour dire que c'est une condition de capture
            return False #Sinon faux
        
        if self.player == 2: #On fait pareil pour le joueur 2
            if self.board[self.user_choice-2] == self.p2_case and self.board[self.user_choice-1] == self.p1_case:
                #Si les pions du joeur 2 encercle les pions du joueur 1 
                self.removed.append(self.board[self.user_choice-1]) #On capture le pion en l'ajoutant à la lsite des pions capturés
                self.board[self.user_choice-1] = self.empty_case #Et en supprimant le pion adverse du plateau du jeu
                return True #Si la condition est vrai on renvoie vraie
            return False #Sinon faux
        

    def possible(self):
        """
        Fonction permettant de déterminer si OUI ou NON il est possible pour le joueur de jouer
        sur une case i choisi.
        """
        self.user_choice = int(input("Choose a number to put your pawn: "))
        for case in self.board: #Pour toutes les cases dans le tableau,
            if self.board[self.user_choice] == self.empty_case and Alak.captured(self) == False: #Si la case est vide et que
                return True
        return False

    
    def select(self):
        """
        Fonction permettant au joueur d'indiquer la case sur laquelle il souhaite
        jouer. S'il est impossible d'y jouer alors on lui demande de choisir une autre case
        sinon la case sélectionnée est valide.
        """
        while Alak.possible(self) != True:
            print("Sorry you can't choose this place, please choose another number to put your pawn")
        self.choice = self.user_choice
        return "Well, you chose the number " + str(self.choice)


    def put(self):
        """
        Fonction qui permet de poser le pion sur la case séléctionné
        """
        Alak.select(self) 

        self.choice = self.user_choice
        if self.player == 1:
            self.board[self.choice] = "x"
            Alak.display(self)
            return True
            
        if self.player == 2:
            self.board[self.choice] = "o"
            Alak.display(self)
            return True
        Alak.display(self)
        return False, "Impossibe de poser un pion" 
        

    def again(self): #A revoir car cette fonction ne fonctionne pas
        """
        Fonction qui permet de vérifier si le 
        joueur peut encore poser un pion sur le plateau
        """
        return Alak.possible(self)   


    def win(self):
        if Alak.again(self) == False:
            p1,p2 = 0,0
            for case in self.board:
                if case == self.p1_case:
                    p1 += 1
                if case == self.p2_case:
                    p2 += 1
            if p1 > p2:
                return "CONGRATULATIONS Player 1 you've won the part !"
            elif p1 < p2:
                return "CONGRATULATIONS Player 2 you've won the part !"
            else:
                return "CONGRATULATIONS you've both won the part ! "
