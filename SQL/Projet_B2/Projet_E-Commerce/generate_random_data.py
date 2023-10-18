from faker import Faker 
import random
faker = Faker('fr_FR')

import sqlite3

""" Generations de donnees aléatoires à inclure dans la BDD, 
    à l'aide de Python et la Bibliothèque Faker qui génère de fausses données,
    et la Bibliothèque Random qui génère des données aléatoires. """

class Ecommerce(): #Classe Ecommerce représentant la base de données e-commerce et ses tables
    def __init__(self):
        self.connected = sqlite3.connect('e-commerce.db')

        self.user_table()
        self.address_table()
        self.payment_table()
        self.product_table()
        self.rate_table()
        self.cart_table()
        self.command_table()
        self.invoices_table()
        self.category_table()

        self.connected.commit()
        self.connected.close()

################################################################################################

    def user_table(self):
        for _ in range(50): #Génération de 50 données dans la table "User"
            self.connected.execute("INSERT INTO User(gender,lastname,firstname,email,date_of_birth,phone_number) VALUES('"+self.gender()+"','"+faker.first_name()+"','"+faker.last_name()+"','"+faker.email()+"','"+faker.date()+"','"+faker.phone_number()+"')")
            #Création des données en fonction des divers éléments présents dans la table (Genre, Nom, Prénom, Email, Date d'Anniversaire)
    def gender(self): #Création d'une fonction conditionnelle gender (=genre) 
        randG = random.randint(1,2)
        if randG >1:return "M" #si randG > 1 = M= Male/Masculin
        else:return"F" #Sinon F = Femme/Female

################################################################################################
#Meme procédure de création pour toutes les tables

    def address_table(self):
        for _ in range(50):
            self.connected.execute("INSERT INTO Address(country,city,mail_address,postal_code,house_num,floor_num) VALUES('"+faker.country()+"','"+faker.city()+"','"+faker.address()+"','"+faker.postcode()+"','"+faker.building_number()+"','"+str(random.randint(0,300))+"')")
    
################################################################################################

    def payment_table(self):
        for _ in range(50):
            hamid = "INSERT INTO Payment VALUES (NULL, '"+'FR'+str(random.randint(2670,3000)+random.randint(1153,3004))+"','"+str(random.randint(2670,3000)+random.randint(1153,3004))+"','"+str(random.randint(100,999))+"','"+faker.date()+"', '"+faker.name()+"', '"+str(random.randint(1,50))+"', '"+str(random.randint(1,50))+"')";
            self.connected.execute(hamid);

################################################################################################

    def product_table(self):
        for _ in range(50):
            self.connected.execute("INSERT INTO Product(price,size,color,stock,name) VALUES('"+
            str(random.randint(1,10000000000))+"','"+str(["S","XS","M","L","XL","XXL"][random.randint(0, 5)])+"','"+faker.postcode()+"','"+faker.color_name()+"','"+faker.first_name_female()+"')")

################################################################################################

    def rate_table(self):
        for _ in range(50):
            self.connected.execute("INSERT INTO Rate VALUES(NULL,'"+str(random.randint(0,10))+"','"+str(random.randint(1,50))+"','"+str(random.randint(1,50))+"')")

################################################################################################

    def cart_table(self):
        for _ in range(50):
            self.connected.execute("INSERT INTO Cart VALUES(NULL,'"+str(random.randint(1,20))+"','"+str(random.randint(1,100))+"', '"+str(random.randint(1,100000))+"','"+str(random.randint(1,50))+"','"+str(random.randint(1,50))+"')")

################################################################################################

    def command_table(self):
        for _ in range(50):
            self.connected.execute("INSERT INTO Command VALUES(NULL,'"+faker.date()+"','"+faker.date()+"', '"+str(random.randint(1,10000000))+"', '"+str(random.randint(1,15))+"','"+str(random.randint(1,100))+"','"+faker.city()+"','"+str(random.randint(1,50))+"','"+str(random.randint(1,50))+"','"+str(random.randint(1,50))+"')")
    
################################################################################################

    def invoices_table(self):
        for _ in range(50):
            self.connected.execute("INSERT INTO Invoices VALUES(NULL,'"+str(random.randint(1,50))+"', '"+str(random.randint(1,50))+"', '"+str(random.randint(1,50))+"','"+str(random.randint(1,50))+"')") 

################################################################################################

    def category_table(self):
        self.connected.execute("INSERT INTO Category (name_category) VALUES ('"+'Robe'+"'),('"+'Jupe'+"'),('"+'Short'+"'), ('"+'Pantalon'+"'),('"+'Top'+"'),('"+'Chemise'+"'),('"+'Pull'+"')")

