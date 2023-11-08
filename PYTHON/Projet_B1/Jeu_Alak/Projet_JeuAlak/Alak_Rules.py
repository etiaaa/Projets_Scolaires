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
        #Pour le joueur 1
        if self.player == 1: 
            #On analyse les deux cases suivantes
            if self.board[self.user_choice+1] == self.p2_case and self.board[self.user_choice+2] == self.p1_case:
                #Si les pions du joueur 1 encercle les pions du joueur 2
                self.removed.append(self.board[self.user_choice+1]) #Alors on capture le pion du joueur 2 en l'ajoutant a la liste des pions capturés
                self.board[self.user_choice+1] = self.empty_case #Et en le supprimant du plateau du jeu
                return True #Si la condition est vrai on renvoie vrai pour dire que c'est une condition de capture
            
            #On analyse la case d'avant et la case après
            elif self.board[self.user_choice-1] == self.p2_case and self.board[self.user_choice+1] == self.p2_case:
                #Si les pions du joueur 1 encercle les pions du joueur 2
                self.removed.append(self.board[self.user_choice]) #Alors on capture le pion du joueur 2 en l'ajoutant a la liste des pions capturés
                self.board[self.user_choice] = self.empty_case #Et en le supprimant du plateau du jeu
                return True #Si la condition est vrai on renvoie vrai pour dire que c'est une condition de capture

            #On analyse les deux cases d'avant
            elif self.board[self.user_choice-1] == self.p2_case and self.board[self.user_choice-2] == self.p1_case:
                #Si les pions du joueur 1 encercle les pions du joueur 2
                self.removed.append(self.board[self.user_choice-1]) #Alors on capture le pion du joueur 2 en l'ajoutant a la liste des pions capturés
                self.board[self.user_choice-1] = self.empty_case #Et en le supprimant du plateau du jeu
                return True #Si la condition est vrai on renvoie vrai pour dire que c'est une condition de capture
            
            #Sinon faux
            else:
                return False 
        
        #On fait pareil pour le joueur 2
        if self.player == 2: 
            #On analyse les deux cases suivantes
            if self.board[self.user_choice+1] == self.p1_case and self.board[self.user_choice+2] == self.p2_case:
                #Si les pions du joueur 1 encercle les pions du joueur 2
                self.removed.append(self.board[self.user_choice+1]) #Alors on capture le pion du joueur 2 en l'ajoutant a la liste des pions capturés
                self.board[self.user_choice+1] = self.empty_case #Et en le supprimant du plateau du jeu
                return True #Si la condition est vrai on renvoie vrai pour dire que c'est une condition de capture
            
            #On analyse la case d'avant et la case après
            elif self.board[self.user_choice-1] == self.p1_case and self.board[self.user_choice+1] == self.p1_case:
                #Si les pions du joueur 1 encercle les pions du joueur 2
                self.removed.append(self.board[self.user_choice]) #Alors on capture le pion du joueur 2 en l'ajoutant a la liste des pions capturés
                self.board[self.user_choice] = self.empty_case #Et en le supprimant du plateau du jeu
                return True #Si la condition est vrai on renvoie vrai pour dire que c'est une condition de capture

            #On analyse les deux cases d'avant
            elif self.board[self.user_choice-1] == self.p1_case and self.board[self.user_choice-2] == self.p2_case:
                #Si les pions du joueur 1 encercle les pions du joueur 2
                self.removed.append(self.board[self.user_choice-1]) #Alors on capture le pion du joueur 2 en l'ajoutant a la liste des pions capturés
                self.board[self.user_choice-1] = self.empty_case #Et en le supprimant du plateau du jeu
                return True #Si la condition est vrai on renvoie vrai pour dire que c'est une condition de capture
            
            #Sinon faux 
            else:
                return False        
        

    def possible(self):
        """
        Fonction permettant de déterminer si OUI ou NON il est possible pour le joueur de jouer
        sur une case i choisi.
        """
        self.user_choice = int(input("Choose a number to put your pawn: "))
        for case in self.board: #Pour toutes les cases dans le tableau,
            if self.board[self.user_choice] == self.empty_case and Alak.captured(self) == False: #Si la case est vide et qu'elle n'a pas été capturé au tour précédent 
                return True #Alors il est possible pour le joueur de poser son pion 
        return False #Sinon il ne peut pas

    
    def select(self):
        """
        Fonction permettant au joueur d'indiquer la case sur laquelle il souhaite
        jouer. S'il est impossible d'y jouer alors on lui demande de choisir une autre case
        sinon la case sélectionnée est valide.
        """
        while Alak.possible(self) != True: #Tant qu'il n'est possible pour le joueur de poser son pion sur la case choisi
            print("Sorry you can't choose this place, please choose another number to put your pawn") #Lui indiquer de choisir une autre case
        self.choice = self.user_choice #Ici on stock la valeur du choix du joueur dans une variable
        return "Well, you chose the number " + str(self.choice) #Et on affiche son choix par la suite


    def put(self):
        """
        Fonction qui permet de poser le pion sur la case séléctionné
        """
        Alak.select(self) #Après avoir séléctionner son pion

        self.choice = self.user_choice #La séléction est conservé dans une variable
        if self.player == 1: #Si c'est le joueur 1
            self.board[self.choice] = "x" #L'emplacement séléctionné est remplacé par le pion du joueur 1
            
        if self.player == 2: #Si c'est le joueur 2
            self.board[self.choice] = "o" #L'emplacement est remplacé par le pion du joueur
        Alak.display(self) #On affiche le plateau du jeu mis à jour
       

    def again(self):
        """
        Fonction qui permet de vérifier si le 
        joueur peut encore poser un pion sur le plateau
        """
        return Alak.possible(self) #On vérifie qu'il est toujours possible pour le joueur de poser un pion
                                   #S'il ne peut pas on sort de la fonction (ce qui reviens a arrêté le jeu)
         


    def win(self):
        """
        Fonction qui permet d'afficher les conditons de victoire 
        si le joueur ne peut plus poser de pion sur le plateau du jeu"""
        p1,p2 = 0,0 #On définit 2 variables qui représenteront le nombre de pions présent sur le plateau pour chaque joueur 
        if Alak.again(self) == False: #Si le joueur ne peut plus poser de pion
            for case in self.board: #Pour toutes les cases sur le plateau de jeu
                if case == self.p1_case: #S'il s'agit d'une case appartenant au joueur 1
                    p1 += 1 #On incrémente d'un
                if case == self.p2_case: #S'il s'agit d'une case appartenant au joueur 2
                    p2 += 1 #On incrémente d'un
            if p1 > p2: #A la fin on vérifie si c'est le joueue 1 qui as le plus de pion
                return "CONGRATULATIONS Player 1 you've won the part !" #Il a gagné
            elif p1 < p2: #Sinon si c'est le joueur 2
                return "CONGRATULATIONS Player 2 you've won the part !" #Il a gagné
            else: #Sinon
                return "CONGRATULATIONS you've both won the part ! " #Egalité
            

#Session Test:

Test = Alak(9)

Test.newBoard()
Test.display()
print("Fonction Possible: ", Test.possible())
print("Fonction Selection: ", Test.select())
print(Test.put())
print("Fonction Again: ", Test.again())
print("Fonction Win: ", Test.win())
