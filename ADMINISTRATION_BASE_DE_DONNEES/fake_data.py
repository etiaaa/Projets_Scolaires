from faker import Faker 
import random
faker = Faker('fr_FR')

import sqlite3

""" Generations de donnees aléatoires à inclure dans la BDD, 
    à l'aide de Python et la Bibliothèque Faker qui génère de fausses données,
    et la Bibliothèque Random qui génère des données aléatoires. """

class MentalHeal(): 
    """
    Classe MentalHeal représentant la base de données différentes personnes atteints
    de traumatismes liées aux attentas en France. 
    """
    def __init__(self):
        self.connected = sqlite3.connect('mental-heal.db')

        self.User()

        self.connected.commit()
        self.connected.close()

################################################################################################

    def gender(self): #Création d'une fonction conditionnelle gender (=genre) 
        randGender = random.randint(1,3)
        if randGender == 1:
            return "Male" #Si RandGender vaut 1 le genre est "Male" soit "Masculin"
        else:
            return "Female" #Sinon RandGender vaut 2 le genre est "Female" soit "Femme"
    
    def cause(self): #Création d'une fonction pour la cause 
        RandCause = faker.city()
        """
        Afin de spécifier de qu'ici il s'agit de la cause du traumatisme 
        nous précédons le nom de la ville par "Attent de" 
        """
        return "Attentat de" + RandCause 

    def User(self):
        for _ in range(50): #Génération de 50 données dans la table "User"
            self.connected.execute("INSERT INTO User(gender, lastname, firstname, address, email, age, origin, cause) VALUES('"+self.gender()+"','"+faker.last_name()+"','"+faker.first_name()+"','"+faker.address()+"','"+faker.email()+"','"+faker.random_int(min=10, max=100)+"','"+faker.country()+"','"+self.cause()+"')")
            #Création des données en fonction des divers éléments présents dans la table (Genre, Nom, Prénom, Email, Date d'Anniversaire)
 
    
################################################################################################

