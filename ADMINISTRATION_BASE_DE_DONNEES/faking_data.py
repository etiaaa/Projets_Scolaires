from faker import Faker
import random
import sqlite3
import unicodedata

faker = Faker('fr_FR')

""" 
Initialisation de fausses donnees aléatoires à inclure dans la B.D.D, 
à l'aide de la Bibliothèque Faker qui génère de fausses données,
et la Bibliothèque Random qui génère des données aléatoires. 
"""

class MentalHeal():
    """
    Classe MentalHeal représentant la base de données différentes personnes atteints
    de traumatismes liées aux attentas en France. 
    """
    def __init__(self):
        self.connected = sqlite3.connect('D:\Etia\CURSUS_SCOLAIRE\PROJETS_SCOLAIRES\ADMINISTRATION_BASE_DE_DONNEES\mental-heal.db')
        
        self.create_table()
        self.Person_Traumatised()
        
        self.connected.commit()
        self.connected.close()

    def create_table(self):
        self.connected.execute('''
            CREATE TABLE IF NOT EXISTS Person_Traumatised (
                ID_PERSON INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                GENDER VARCHAR(100),
                LASTNAME VARCHAR(100),
                FIRSTNAME VARCHAR(100),
                ADDRESS VARCHAR(100),
                EMAIL VARCHAR(100),
                AGE INT NOT NULL,
                ORIGIN VARCHAR(100),
                CAUSE VARCHAR(100),
                FOREIGN KEY(CAUSE) REFERENCES Terrorist_Attack(CITY)
            );
        ''')

    def clean_text(self, text):
        return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

    def gender(self):
        gender = random.randint(0, 1)
        if gender == 0:
            return "Male"
        else:
            return "Female"

    def first_name(self, gender):
        if gender == "Male":
            return faker.first_name_male()
        else:
            return faker.first_name_female()

    def cause(self):
        RandCause = faker.city()
        return "Attentat de " + RandCause

    def city(self):
        cursor = self.connected.cursor()
        cursor.execute("SELECT DISTINCT CITY FROM Terrorist_Attack")
        cities = [row[0] for row in cursor.fetchall()]
        return cities

    def email(self, first_name, last_name):
        email_domains = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@free.fr"]
        selected_domain = random.choice(email_domains)
        email = f"{first_name.lower()}.{last_name.lower()}{selected_domain}"
        return email

    def Person_Traumatised(self):
        for _ in range(5000): #Génération de 5000 données dans la table "mental-heal"
            #Création des données en fonction des divers éléments présents dans la table (Genre, Nom, Prénom, Email, Date d'Anniversaire)       
            cause = "Attentat de " + random.choice(self.city())
            gender = self.gender()
            first_name = self.first_name(gender)
            last_name = faker.last_name()
            address = self.clean_text(faker.address())
            email = self.email(first_name, last_name)
            age = str(faker.random_int(min=10, max=100))
            origin = faker.country()

            self.connected.execute("INSERT INTO Person_Traumatised(GENDER, LASTNAME, FIRSTNAME, ADDRESS, EMAIL, AGE, ORIGIN, CAUSE) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                                  (gender, last_name, first_name, address, email, age, origin, cause))

Test = MentalHeal()
Test.Person_Traumatised()