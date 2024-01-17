from faker import Faker
import random
import sqlite3
import unicodedata

faker = Faker('fr_FR')

""" 
Initialisation de fausses donnees aléatoires à inclure dans la BDD, 
à l'aide de la Bibliothèque Faker qui génère de fausses données,
et la Bibliothèque Random qui génère des données aléatoires. 
"""

class MentalHeal():
    """
    Classe MentalHeal représentant la base de données différentes personnes atteints
    de traumatismes liées aux attentas en France. 
    """
    def __init__(self):
        #Ci-dessous connexion a la base de données
        self.connected = sqlite3.connect('D:\Etia\CURSUS_SCOLAIRE\PROJETS_SCOLAIRES\ADMINISTRATION_BASE_DE_DONNEES\MentalHeal.db')
        
        self.create_table() #Fonction qui génèrera la table Person_Traumatised si elle n'existe pas
        self.Person_Traumatised() #Fonction qui génèrera les fausses donnéees aléatoires de la table Person_Traumatised
        
        self.connected.commit() #instruction qui permet qu'une fois les modification sont établis de les appliqués dans la table de la base de donnée
        self.connected.close() #Instruction qui permet de fermer la base de donnée

    def create_table(self): 
        """
        On applique simplement une requete de création de table en veillant à respecter la structure requise par Python
        """
        self.connected.execute('''
            CREATE TABLE IF NOT EXISTS Person_Traumatised (
                ID_PERSON INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                GENDER VARCHAR(100),
                LASTNAME VARCHAR(100),
                FIRSTNAME VARCHAR(100),
                ADDRESS VARCHAR(100),
                CITY VARCHAR(100),
                POSTAL_CODE VARCHAR(100),
                EMAIL VARCHAR(100),
                AGE INT NOT NULL,
                ORIGIN VARCHAR(100),
                CAUSE VARCHAR(100),
                FOREIGN KEY(CAUSE) REFERENCES Terrorist_Attack(CITY)
            );
        ''')

    def clean_text(self, text): 
        """
        Création de la fonction clean_text qui permettra à l'aide de la bibliothèque unicodedata
        d'ignorer les caractères spéciaux qui peuvent être générer dans les données
        """
        return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

    def gender(self):
        """
        Création de la table gender qui renvoie "Male" si le genre vaut 0 et Feminin s'il vaut 1
        """
        gender = random.randint(0, 1)
        if gender == 0:
            return "Male"
        else:
            return "Female"

    def first_name(self, gender):
        """
        Fonction first_name qui permet de générer un prénom féminin ou masculin en prenant compte
        du genre attribué à une personne
        """
        if gender == "Male":
            return faker.first_name_male()
        else:
            return faker.first_name_female()

    def cause(self):
        """
        Fonction cause qui permet de définir la cause (le déclanchement) du traumatisme d'une personne
        en veillant a prendre en compte les villes d'attentats présentes dans la table Terrorist_Attack
        """
        RandCause = faker.city()
        return "Attentat de " + RandCause

    def city(self):
        """
        Fonction qui permet de générer le choix des villes a partir des villes de la table Terrorist_Attack
        """
        cursor = self.connected.cursor()
        cursor.execute("SELECT DISTINCT CITY FROM Terrorist_Attack")
        cities = [row[0] for row in cursor.fetchall()]
        return cities

    def email(self, first_name, last_name):
        """
        Fonction qui permet de générer des emails en utilisant une tranche d'email donnée 
        (afin d'éviter d'avoir "@example.com")
        """
        email_domains = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@free.fr"]
        selected_domain = random.choice(email_domains)
        email = f"{first_name.lower()}.{last_name.lower()}{selected_domain}"
        return email

    def Person_Traumatised(self):
        """
        Fonction qui génère les données à insérer dans la table en prenant en compte 
        les différentes fonctions définient précédemment
        """
        for _ in range(5000): #Génération de 5000 données dans la table "mental-heal"
            cause = "Attentat de " + random.choice(self.city())
            gender = self.gender()
            first_name = self.first_name(gender)
            last_name = faker.last_name()
            address = self.clean_text(faker.street_address())
            city = self.clean_text(faker.city())
            postal_code = faker.postcode()
            email = self.email(first_name, last_name)
            age = str(faker.random_int(min=10, max=100))
            origin = faker.country()
            
            #Ci-dessous ajouts des divers données dans les éléments correspondant de la table 
            self.connected.execute("INSERT INTO Person_Traumatised(GENDER, LASTNAME, FIRSTNAME, ADDRESS, CITY, POSTAL_CODE, EMAIL, AGE, ORIGIN, CAUSE) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                  (gender, last_name, first_name, address, city, postal_code, email, age, origin, cause))
    

Test = MentalHeal() #Génération d'une instance de la classe pour exécuter les données
Test.Person_Traumatised() #Utilisation de la fonction

