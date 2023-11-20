from script1 import *
import sqlite3

# Connectez-vous à la base de données SQLite
conn = sqlite3.connect('script2.db')

# Créez un curseur pour exécuter des requêtes SQL
c = conn.cursor()

# Insérez les données dans une table
table_sql = "Tableau"
for champs in tableau:
  nom = champs[0]
  prix = champs[1]
  c.execute("INSERT INTO " + table_sql + " (nom, prix) VALUES (?, ?)", (nom, prix))

# Confirmez chaque insertion
conn.commit()

# Fermez la connexion à la base de données
conn.close()
