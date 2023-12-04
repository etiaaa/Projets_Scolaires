from JustGetTen_Rules import * #Import du fichier contenant les règles du jeu JustGetTen
#Ci-dessous import de la bibliothèque tkinter qui permettra la création de l'interface
from tkinter import *
import tkinter as tk

class GUI_JustGetTen: #Création de la classe d'interface graphique du jeu JustGetTen

    def __init__(self, JustGetTen):
        """
        Fonction de base permettant d'initier les éléments utiles lors de la création de la classe 
        """
        self.window = Tk() #Création de la fenêtre du jeu
        self.window.title("JustGetTen") #Fenetre du jeu nommé "JustGetTen"
        # self.window.config(bg="black") #Fenêtre ayant un fond blanc
        self.board = Canvas(self.window, width=395, height=390) #Personnalisation des dimensions de la fenêtre du jeu
        self.board.pack() #Affichage du canvas dans la fenêtre
        self.JustGetTen = JustGetTen #Référence à la classe (du fichier externe) JustGetTen
        self.buttons = []  # Créez une liste pour stocker les boutons


    def displayGrid(self): 
        """
        Fonction permettant l'affichage de la grille du jeu
        """
        self.board.place(x=150, y=150)
        getGrid = self.JustGetTen.grid #Référence à la grille du jeu
        button_size = 50 #Initialisation de la taille de nos cases(/boutons)        
        for ligne in range(len(getGrid)): #Pour les lignes qui sont dans la grille
            for colonne in range(len(getGrid[ligne])): #Et les colonnes qui sont dans la grille (les colonnes comprises dans la largeur de la ligne)
                self.case_ligne = ligne * button_size #Multiplication du nombre de bouton en fonction du nombre de lignes présentes 
                self.case_colonne = colonne * button_size #Multiplication du nombre de bouton en fonction du nombre de colonnes présentes 
                self.button = Button(self.board, text=str(getGrid[ligne][colonne]), width=6, height=3, command=lambda v=getGrid[ligne][colonne], l=ligne, c=colonne: self.button_click(v, l, c)) #Création d'un bouton comportant les données présentes dans la grille placée dans le canvas (avec la dimension du bouton)
                self.board.create_window(self.case_ligne, self.case_colonne, window=self.button, anchor="nw") #Ajout des boutons dans le canvas
                self.buttons.append(self.button) #On ajoute le bouton dans une liste de boutons


    def button_click(self, value, ligne, column):
        """
        Fonction qui permet de récuperer les informations (position et valeur) sur la case séléctionner
        """
        print(f"La position de la case séléctionnée est de ({ligne}, {column}), et sa valeur est de {value}.")


    def colorNumber(self):
        """
        Fonction qui permet d'attribuer les couleurs aux différentes cases de la grille
        en fonction du numéro de la case.
        """
        current_case = 0 #On initialise la case actuelle à évaluer
        for ligne in self.JustGetTen.grid: #Pour la ligne dans la grille
            for value_case in ligne: #Pour la case dans la ligne de la grille
                self.button = self.buttons[current_case] #Pour le bouton de la case actuelle
                current_case += 1 #On incrémente la case de 1 à chaque fois (au premier tour la case est donc de 1 pour la première case) 
                #En fonction de la valeur de la case ajouter une couleur 
                if value_case == 1: 
                    self.button.configure(bg="#C74AD6") 
                elif value_case == 2: 
                    self.button.configure(bg="#D64AB4") 
                elif value_case == 3:
                    self.button.configure(bg="#D64A8C")
                elif value_case == 4:
                    self.button.configure(bg="#D64A68")
    
    def StateCase(self): 
        #Fonction qui permet de vérifier l'état des cases adjacentes d'une case choisi
        merge_case = []
        # for lignes in self.JustGetTen.grid:
        #     if lignes == lignes[0]:
        #         for self.button in self.grid:
        #             if lignes[self.button+1] == lignes[self.button]:
        #                 merge_case.append(self.button)
        # print(merge_case)    

    def displayGameBoard(self): 
        """
        Fonction qui permet d'afficher le plateau du jeu dans la fenêtre
        """
        GUI_JustGetTen.displayGrid(self) #Appel de la fonction displayGrid crée juste au dessus
        GUI_JustGetTen.colorNumber(self)
        GUI_JustGetTen.StateCase(self)
        self.window.mainloop() #affichage de la fenetre


#Session Test:

Game = JustGetTen()  # Créez une instance de JustGetTen
Gui = GUI_JustGetTen(Game)  # Passez l'instance de JustGetTen à GUI_JustGetTen
Gui.displayGameBoard()  # Affichez la fenêtre avec la grille
