import tkinter as tk
from tkinter import messagebox
import sqlite3
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from docx import Document
from docx.shared import Inches
from PIL import Image
import io

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestion des Utilisateurs")

        self.couleur_fond_degrade = ("#ffcc00", "#ff6600")

        self.canvas = tk.Canvas(self.master, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.master.bind("<Configure>", self.redimensionner_fond)

        self.creer_fond_degrade()

        self.creer_base_de_donnees()

        self.creer_menu_gauche()

    def creer_menu_gauche(self):
        menu_frame = tk.Frame(self.master, bg="#333")
        menu_frame.place(relx=0, rely=0, relwidth=0.2, relheight=1)  
        bouton_fichier = tk.Button(menu_frame, text="Quitter", command=self.demander_confirmation_quitter, bg="#444", fg="white")
        bouton_fichier.pack(side=tk.TOP, fill=tk.X)
        
        bouton_donnees = tk.Button(menu_frame, text="Données", bg="#444", fg="white", state=tk.DISABLED)
        bouton_donnees.pack(side=tk.TOP, fill=tk.X)

        groupe_options = tk.LabelFrame(menu_frame, text="Options Données", bg="#333", fg="white", padx=5, pady=5)
        groupe_options.pack(side=tk.TOP, fill=tk.X)

        bouton_obtenir_stocker = tk.Button(groupe_options, text="Obtenir et Stocker les données (100)", command=self.obtenir_et_stocker_utilisateurs, bg="#444", fg="white")
        bouton_obtenir_stocker.pack(side=tk.TOP, fill=tk.X)

        bouton_supprimer_contenu_bdd = tk.Button(groupe_options, text="Supprimer Contenu BDD", command=self.supprimer_contenu_base_de_donnees, bg="#444", fg="white")
        bouton_supprimer_contenu_bdd.pack(side=tk.TOP, fill=tk.X)

        bouton_afficher_total = tk.Button(groupe_options, text="Afficher Total Utilisateurs", command=self.afficher_total_utilisateurs, bg="#444", fg="white")
        bouton_afficher_total.pack(side=tk.TOP, fill=tk.X)

        bouton_graphiques = tk.Button(menu_frame, text="Graphiques", bg="#444", fg="white", command=self.obtenir_et_afficher_graphiques)
        bouton_graphiques.pack(side=tk.TOP, fill=tk.X)

        groupe_options_graphiques = tk.LabelFrame(menu_frame, text="Options Graphiques", bg="#333", fg="white", padx=5, pady=5)
        groupe_options_graphiques.pack(side=tk.TOP, fill=tk.X)

        bouton_graphique1 = tk.Button(groupe_options_graphiques, text="Taux Homme/Femme", command=self.afficher_taux_homme_femme, bg="#444", fg="white")
        bouton_graphique1.pack(side=tk.TOP, fill=tk.X)

        bouton_graphique2 = tk.Button(groupe_options_graphiques, text="Diversité des Pays", command=self.afficher_diversite_pays, bg="#444", fg="white")
        bouton_graphique2.pack(side=tk.TOP, fill=tk.X)

        bouton_graphique3 = tk.Button(groupe_options_graphiques, text="Moyenne d'Âges", command=self.afficher_moyenne_ages, bg="#444", fg="white")
        bouton_graphique3.pack(side=tk.TOP, fill=tk.X)

        bouton_theme = tk.Button(menu_frame, text="Thème", bg="#444", fg="white")
        bouton_theme.pack(side=tk.TOP, fill=tk.X)

        groupe_options_theme = tk.LabelFrame(menu_frame, text="Options Thème", bg="#333", fg="white", padx=5, pady=5)
        groupe_options_theme.pack(side=tk.TOP, fill=tk.X)

        bouton_theme1 = tk.Button(groupe_options_theme, text="Thème 1", command=self.changer_theme_1, bg="#444", fg="white")
        bouton_theme1.pack(side=tk.TOP, fill=tk.X)

        bouton_theme2 = tk.Button(groupe_options_theme, text="Thème 2", command=self.changer_theme_2, bg="#444", fg="white")
        bouton_theme2.pack(side=tk.TOP, fill=tk.X)

        bouton_theme3 = tk.Button(groupe_options_theme, text="Thème 3", command=self.changer_theme_3, bg="#444", fg="white")
        bouton_theme3.pack(side=tk.TOP, fill=tk.X)

    def demander_confirmation_quitter(self):
        confirmation = messagebox.askokcancel("Confirmation", "Voulez-vous vraiment quitter l'application?")
        if confirmation:
            self.quitter()

    def creer_fond_degrade(self):
        self.canvas.delete("all")

        for i in range(256):
            proportion = i / 255.0
            couleur = self.interpoler_couleurs(self.couleur_fond_degrade[0], self.couleur_fond_degrade[1], proportion)
            x0 = 0
            x1 = self.canvas.winfo_width()
            y0 = i * (self.canvas.winfo_height() / 255)
            y1 = (i + 1) * (self.canvas.winfo_height() / 255)
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=couleur, outline="")

    def redimensionner_fond(self, event):
        self.creer_fond_degrade()

    def interpoler_couleurs(self, couleur1, couleur2, proportion):
        r1, g1, b1 = int(couleur1[1:3], 16), int(couleur1[3:5], 16), int(couleur1[5:7], 16)
        r2, g2, b2 = int(couleur2[1:3], 16), int(couleur2[3:5], 16), int(couleur2[5:7], 16)
        r = int(r1 + proportion * (r2 - r1))
        g = int(g1 + proportion * (g2 - g1))
        b = int(b1 + proportion * (b2 - b1))
        return f"#{r:02x}{g:02x}{b:02x}"

    def creer_base_de_donnees(self):
        try:
            conn = sqlite3.connect("./utilisateurs.db")
            cursor = conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            genre TEXT,
                            prenom TEXT,
                            nom TEXT,
                            email TEXT,
                            pays TEXT,
                            age INTEGER)''')

            conn.commit()
            conn.close()

        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la création de la base de données : {str(e)}")

    def obtenir_et_stocker_utilisateurs(self):
        try:
            url = "https://randomuser.me/api/"
            params = {"results": 100}
            response = requests.get(url, params=params)
            data = response.json()

            utilisateurs = data.get("results", [])

            if utilisateurs:
                conn = sqlite3.connect("./utilisateurs.db")
                cursor = conn.cursor()

                for utilisateur in utilisateurs:
                    genre = utilisateur.get("gender", "")
                    prenom = utilisateur.get("name", {}).get("first", "")
                    nom = utilisateur.get("name", {}).get("last", "")
                    email = utilisateur.get("email", "")
                    pays = utilisateur.get("location", {}).get("country", "")
                    age = utilisateur.get("dob", {}).get("age", 0)

                    cursor.execute("INSERT INTO utilisateurs (genre, prenom, nom, email, pays, age) VALUES (?, ?, ?, ?, ?, ?)",
                                   (genre, prenom, nom, email, pays, age))

                conn.commit()
                conn.close()

                messagebox.showinfo("Succès", "Les utilisateurs ont été récupérés et stockés avec succès.")

            else:
                messagebox.showwarning("Avertissement", "Aucun utilisateur trouvé.")

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite lors de la récupération des utilisateurs : {str(e)}")

    def supprimer_contenu_base_de_donnees(self):
        confirmation = messagebox.askokcancel("Confirmation", "Voulez-vous vraiment supprimer le contenu de la base de données?")
        if confirmation:
            try:
                conn = sqlite3.connect("./utilisateurs.db")
                cursor = conn.cursor()

                cursor.execute("DELETE FROM utilisateurs")
                conn.commit()
                conn.close()

                messagebox.showinfo("Succès", "Le contenu de la base de données a été supprimé avec succès.")

            except Exception as e:
                messagebox.showerror("Erreur", f"Une erreur s'est produite lors de la suppression du contenu de la base de données : {str(e)}")

    def afficher_total_utilisateurs(self):
        try:
            conn = sqlite3.connect("./utilisateurs.db")
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM utilisateurs")
            total_utilisateurs = cursor.fetchone()[0]

            conn.close()

            messagebox.showinfo("Total Utilisateurs", f"Le total des utilisateurs dans la base de données est de {total_utilisateurs}.")

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite lors de l'obtention du total des utilisateurs : {str(e)}")

    def obtenir_et_afficher_graphiques(self):
        try:
            conn = sqlite3.connect("./utilisateurs.db")
            cursor = conn.cursor()
            cursor.execute("SELECT genre, pays, age FROM utilisateurs")
            data = cursor.fetchall()
            conn.close()

            self.afficher_taux_homme_femme(data)
            self.afficher_diversite_pays(data)
            self.afficher_moyenne_ages(data)

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

    def afficher_taux_homme_femme(self):
        try:
            conn = sqlite3.connect("./utilisateurs.db")
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM utilisateurs WHERE genre='male'")
            hommes = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM utilisateurs WHERE genre='female'")
            femmes = cursor.fetchone()[0]

            conn.close()

            labels = ['Hommes', 'Femmes']
            values = [hommes, femmes]

            fig, ax = plt.subplots()
            ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.set_title('Taux d\'Hommes et de Femmes')
            self.afficher_graphique(fig)

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")


    def afficher_diversite_pays(self):
        try:
            conn = sqlite3.connect("./utilisateurs.db")
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(DISTINCT pays) FROM utilisateurs")
            diversite_pays = cursor.fetchone()[0]

            conn.close()

            labels = ['Diversité des Pays']
            values = [diversite_pays]

            fig, ax = plt.subplots()
            ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.set_title('Diversité des Pays')
            self.afficher_graphique(fig)

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")


    def afficher_moyenne_ages(self):
        try:
            conn = sqlite3.connect("utilisateurs.db")
            cursor = conn.cursor()
            cursor.execute("SELECT AVG(age) FROM utilisateurs")
            moyenne_ages = cursor.fetchone()[0]

            conn.close()

            labels = ['Moyenne d\'âges']
            values = [moyenne_ages]

            fig, ax = plt.subplots()
            ax.bar(labels, values)
            ax.set_ylabel('Âge moyen')
            ax.set_title('Moyenne d\'Âges')
            self.afficher_graphique(fig)

        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

    def afficher_graphique(self, fig):
        new_window = tk.Toplevel(self.master)
        new_window.title("Graphique")

        canvas = FigureCanvasTkAgg(fig, master=new_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, new_window)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def changer_theme_1(self):
        self.couleur_fond_degrade = ("#ffcc00", "#ff6600")
        self.creer_fond_degrade()

    def changer_theme_2(self):
        self.couleur_fond_degrade = ("#ff9900", "#ff3300")
        self.creer_fond_degrade()

    def changer_theme_3(self):
        self.couleur_fond_degrade = ("#ff0000", "#ff99cc")
        self.creer_fond_degrade()

    def quitter(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.geometry("800x600")
    root.protocol("WM_DELETE_WINDOW", app.demander_confirmation_quitter)
    root.mainloop()
