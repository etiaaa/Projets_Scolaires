######################################## Consigne ##########################################
"""
5 - (2 points) - Trouver une solution afin que lorsque que le bot s'arrête ses données stockées dans les différentes structures et collections crées précédement se soient pas perdues.
Vous êtes libre d'utiliser ce que vous voulez pour stocker les données, un fichier texte, un fichier Json, une base de données ...
"""

# Import des modules nécessaires soit tous ainsi que de la bibliothèque json
from Historique import *
from Conversation import *
import json

# Création de la fonction "save_data" qui permet la sauvegarde des données
# dans un fichier défini à un emplacement 
def save_data(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)


# Création de la fonction "load_data" qui permet le chargement des données
# à partir d'un fichier défini à un emplacement 
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Création d'une instance du code
history = HistoryManager()
conversations = Conversation()

# Chargement des données au démarrage du bot
history_data = load_data("history_data.json")
conversations_data = load_data("conversations_data.json")

history.load_from_data(history_data)
conversations.load_from_data(conversations_data)

# Sauvegarde des données à l'arrêt du bot
history_data = history.get_data()
conversations_data = conversations.get_data()

save_data(history_data, "history_data.json")
save_data(conversations_data, "conversations_data.json")