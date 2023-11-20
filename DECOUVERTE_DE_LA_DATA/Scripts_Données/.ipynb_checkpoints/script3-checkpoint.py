#Import des modules nécessaires à savoir sqlite3, pandas, streamlite et plotly.

import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

#Création d'une variable conn pour configurer une connexion à la base de données SQLite.
conn = sqlite3.connect('script2.db')

#Création d'une variable bd qui permet la lecture des données depuis la base de données
bd = pd.read_sql_query("SELECT * from Tableau", conn)

#Affichage du tableau dans Streamlit
st.write("Tableau de données : ")
st.dataframe(bd)

# Affichage du graphique à barres
fig = px.bar(bd, x='nom', y='prix')
st.write("Graphique à barres : ")
st.plotly_chart(fig)

#Affichage du graphique en courbe
fig = px.line(bd, x='nom', y='prix')
st.write("Graphique en courbe : ")
st.plotly_chart(fig)

#Fermeture de la connexion à la base de données.
conn.close()


#Pour ouvrir le tableau dans streamlit taper la commande suivante: streamlit run .\script3.py ou excéctuter le lien suivant: http://localhost:8506.