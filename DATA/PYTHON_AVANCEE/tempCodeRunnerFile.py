import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog
from bs4 import BeautifulSoup
from urllib.parse import unquote
import matplotlib.pyplot as plt
from docx.shared import Inches
from PIL import Image, ImageTk
from docx import Document
import tkinter.simpledialog  
import requests
import io
import os

class gutenbergApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Mon Application")
        self.geometry("800x600")

        # Création de l'interface utilisateur
        self.creer_interface()

    def creer_interface(self):
        # Frame principale
        frame_principal = ttk.Frame(self)
        frame_principal.pack(fill=tk.BOTH, expand=True)

        # Création d'un widget Text pour afficher les informations du livre
        self.texte_info_livre = scrolledtext.ScrolledText(frame_principal, wrap=tk.WORD, width=40, height=10)
        self.texte_info_livre.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Création d'un bouton pour télécharger le livre et afficher les informations
        bouton_telecharger_livre = ttk.Button(frame_principal, text="Télécharger le Livre", command=self.telecharger_et_afficher_livre)
        bouton_telecharger_livre.pack(pady=10)

        # Création d'un bouton pour générer le graphe
        bouton_generer_graphe = ttk.Button(frame_principal, text="Générer le Graphe", command=self.generer_graphe)
        bouton_generer_graphe.pack(pady=10)

        # Création d'un bouton pour télécharger l'image depuis Internet
        bouton_telecharger_image = ttk.Button(frame_principal, text="Télécharger l'Image", command=self.telecharger_image)
        bouton_telecharger_image.pack(pady=10)

        # Ajoutez le bouton pour recadrer l'image
        bouton_recadrer_image = ttk.Button(frame_principal, text="Recadrer l'Image", command=lambda: self.recadrer_redimensionner_image(0.8, 0.8))
        bouton_recadrer_image.pack(pady=10)

        # Ajouter le bouton pour lire et manipuler l'image
        bouton_manipuler_image = ttk.Button(frame_principal, text="Manipuler l'Image", command=self.manipuler_image)
        bouton_manipuler_image.pack(pady=10)

        # Variable pour stocker le premier chapitre
        self.premier_chapitre_livre = ""

    def telecharger_et_afficher_livre(self):
        chemin_fichier = filedialog.askopenfilename(title="Sélectionner le fichier texte", filetypes=[("Fichiers texte", "*.txt")])

        if chemin_fichier:
            contenu_livre = self.telecharger_livre(chemin_fichier)

            if contenu_livre:
                # Extraire les informations du livre
                titre_livre, auteur_livre, self.premier_chapitre_livre = self.extraire_informations_livre(contenu_livre)

                # Afficher les informations dans le widget Text
                self.texte_info_livre.delete(1.0, tk.END)
                self.texte_info_livre.insert(tk.END, f"Titre du livre : {titre_livre}\n")
                self.texte_info_livre.insert(tk.END, f"Auteur du livre : {auteur_livre}\n")
                self.texte_info_livre.insert(tk.END, f"Premier chapitre du livre :\n{self.premier_chapitre_livre[:500]}...")  # Afficher les 500 premiers caractères pour aperçu

    def telecharger_livre(self, chemin_fichier):
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as file:
                contenu_livre = file.read()
                return contenu_livre
        except Exception as e:
            print(f"Une erreur s'est produite lors de la lecture du fichier : {str(e)}")
            return None

    def extraire_informations_livre(self, contenu_livre):
        debut_titre = contenu_livre.find("*** START OF THIS PROJECT GUTENBERG EBOOK") + len("*** START OF THIS PROJECT GUTENBERG EBOOK")
        fin_titre = contenu_livre.find("by", debut_titre)
        titre = contenu_livre[debut_titre:fin_titre].strip()

        debut_auteur = fin_titre + len("by")
        fin_auteur = contenu_livre.find("\n", debut_auteur)
        auteur = contenu_livre[debut_auteur:fin_auteur].strip()

        debut_premier_chapitre = contenu_livre.find("CHAPTER I.") + len("CHAPTER I.")
        premier_chapitre = contenu_livre[debut_premier_chapitre:debut_premier_chapitre + 500].strip()

        return titre, auteur, premier_chapitre

    def generer_graphe(self):
        if self.premier_chapitre_livre:
            # Compter le nombre de mots dans chaque paragraphe
            longueurs_paragraphes = [len(paragraphe.split()) // 10 * 10 for paragraphe in self.premier_chapitre_livre.split('\n') if paragraphe.strip()]

            # Créer un histogramme pour montrer la distribution des longueurs des paragraphes
            plt.hist(longueurs_paragraphes, bins=range(min(longueurs_paragraphes), max(longueurs_paragraphes) + 10, 10), edgecolor='black')
            plt.xlabel('Longueur des Paragraphes (par dizaines de mots)')
            plt.ylabel('Nombre de Paragraphes')
            plt.title('Distribution des Longueurs des Paragraphes du Premier Chapitre')
            plt.show()
        else:
            print("Le premier chapitre du livre n'est pas chargé.")

    def telecharger_image(self):
        url_image = "https://www.gutenberg.org/cache/epub/64202/pg64202.cover.medium.jpg"

        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            response = requests.get(url_image, headers=headers)

            if response.status_code == 200:
                # Enregistrez l'image dans le dossier du script
                image_path = os.path.join(os.path.dirname(__file__), "Project_image.jpg")
                with open(image_path, 'wb') as image_file:
                    image_file.write(response.content)

                print("L'image a été téléchargée et enregistrée avec succès.")
                
                # Proposez à l'utilisateur d'ouvrir le fichier téléchargé
                reponse = tk.messagebox.askyesno("Ouvrir l'image", "Voulez-vous ouvrir l'image téléchargée?")
                if reponse:
                    img = Image.open(image_path)
                    img.show()
            else:
                print(f"Échec du téléchargement de l'image. Statut de la requête : {response.status_code}")
        except Exception as e:
            print(f"Une erreur s'est produite lors du téléchargement de l'image : {str(e)}")
        self.recadrer_redimensionner_image(-30, -30)  # Les facteurs de 0.8 sont des exemples, ajustez-les selon vos besoins

    def recadrer_redimensionner_image(self, facteur_largeur, facteur_hauteur):
        image_path = os.path.join(os.path.dirname(__file__), "Project_image.jpg")

        try:
            # Ouvrez l'image
            img = Image.open(image_path)

            # Obtenez les dimensions actuelles de l'image
            largeur_actuelle, hauteur_actuelle = img.size

            # Calculez les nouvelles dimensions
            nouvelle_largeur = int(largeur_actuelle * facteur_largeur)
            nouvelle_hauteur = int(hauteur_actuelle * facteur_hauteur)

            # Recadrez et redimensionnez l'image
            img = img.resize((nouvelle_largeur, nouvelle_hauteur))

            # Enregistrez l'image redimensionnée avec un nouveau nom de fichier
            image_redimensionnee_path = os.path.join(os.path.dirname(__file__), "Project_recadrement-image.jpg")
            img.save(image_redimensionnee_path)

            print("L'image a été recadrée et redimensionnée avec succès.")

            # Proposez à l'utilisateur d'ouvrir le fichier recadré et redimensionné
            reponse = tk.messagebox.askyesno("Ouvrir l'image recadrée", "Voulez-vous ouvrir l'image recadrée?")
            if reponse:
                img_resized = Image.open(image_redimensionnee_path)
                img_resized.show()
        except Exception as e:
            print(f"Une erreur s'est produite lors du recadrage et redimensionnement de l'image : {str(e)}")

        def manipuler_image(self):
            # Charger l'image en noir et blanc
            image_path = os.path.join(os.path.dirname(__file__), "Project_image.jpg")
            img = Image.open(image_path).convert('L')

            # Obtenir l'angle de rotation depuis l'utilisateur
            angle_rotation = tkinter.simpledialog.askfloat("Entrer un angle", "Veuillez entrer l'angle de rotation :")

            if angle_rotation is not None:
                # Faire pivoter l'image selon l'angle spécifié
                img_rotated = img.rotate(angle_rotation)

                # Sauvegarder l'image pivotée dans un fichier nommé "photo1.jpg"
                file_path_photo1 = os.path.join(os.path.dirname(__file__), "photo1.jpg")
                img_rotated.save(file_path_photo1)

                print(f"L'image a été pivotée de {angle_rotation} degrés et enregistrée dans le fichier photo n°1.")

if __name__ == "__main__":
    app = gutenbergApp()
    app.mainloop()
