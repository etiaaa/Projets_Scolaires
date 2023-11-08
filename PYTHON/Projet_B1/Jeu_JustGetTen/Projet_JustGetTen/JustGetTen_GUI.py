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
        self.window.config(bg="black") #Fenêtre ayant un fond blanc
        self.board = Canvas(self.window, width=1200, height=650) #Personnalisation des dimensions de la fenêtre du jeu
        self.board.pack() #Affichage du canvas dans la fenêtre
        self.JustGetTen = JustGetTen #Référence à la classe (du fichier externe) JustGetTen


    def displayGrid(self): 
        """
        Fonction permettant l'affichage de la grille du jeu
        """
        Grid = self.JustGetTen.grid #Référence à la grille du jeu
        button_size = 50 #Initialisation de la taille de nos cases(/boutons) 
        for lignes in range(len(Grid)): #Pour les lignes qui sont dans la grille
            for colonnes in range(len(Grid[lignes])): #Et les colonnes qui sont dans la grille (les colonnes comprises dans la largeur de la ligne)
                case_ligne, case_colonne = colonnes * button_size, lignes * button_size #Multipliez le nombre de cases en ligne et en colonne par le nombre de ligne et colonne existante
                button = Button(self.board, text=str(Grid[lignes][colonnes]), width=5, height=2) #Création d'un bouton comportant les données présentes dans la grille placée dans le canvas (avec la dimension du bouton)
                self.board.create_window(case_ligne, case_colonne, window=button, anchor="nw") #Ajout des boutons dans le canvas
        

    # def colorNumber(self):
    #     for case in self.JustGetTen.grid:
    #         if case_ligne or case_colonne == 1:
    #                 button.configure(bg="#CC87B2")
    #         if case_ligne or case_colonne == "2":
    #                 button.configure(bg="#C787CC")
    #         if case_ligne or case_colonne == "3":
    #                 button.configure(bg="#A387CC")
    #         else:
    #             button.configure(bg="#8E87CC")


    def displayGameBoard(self): 
        """
        Fonction qui permet d'afficher le plateau du jeu dans la fenêtre
        """
        self.displayGrid() #Appel de la fonction displayGrid crée juste au dessus
        self.window.mainloop() #affichage de la fenetre


#Session Test:

Game = JustGetTen()  # Créez une instance de JustGetTen
Gui = GUI_JustGetTen(Game)  # Passez l'instance de JustGetTen à GUI_JustGetTen

# Gui.colorNumber()  # Affichez la fenêtre avec la grille
Gui.displayGameBoard()  # Affichez la fenêtre avec la grille
