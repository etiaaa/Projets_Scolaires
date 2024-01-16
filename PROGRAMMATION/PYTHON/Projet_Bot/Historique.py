######################################## Consigne ##########################################
"""
1 - (4 points) - Via une liste chainée, une pile ou une file, créer un système de d'historique des commandes de votre bot. Ce système devra avoir comme fonctionnalités :
    - de quoi voir la dernière commande rentrée
    - de quoi voir toutes les commandes rentrée par un utilisateur depuis sa première connexion
    - de quoi se déplacer dans cet historique (en avant et en arrière)
    - de quoi vider l'historique
"""

#CE CODE A ETE FAIT A L'AIDE DU CODE DU PROF

# Import des modules nécessaires pour utiliser la bibliothèque Discord et ses extensions.
import discord 
from discord.ext import commands


# Cration d'une classe Node qui représente un nœud de la liste chaînée. 
# Chaque nœud contient une donnée: "data", et une référence vers le prochain nœud: "next_node".
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


# Créaation d'une classe ChainedList représente une liste chaînée et est composée de nœuds. 
# "first_node" qui représente le dernier noeud et "last_node" le dernier nœud. 
# "size" représente le nombre de nœuds dans la liste donc au départ 1.
class ChainedList:
    #__init__" : méthode d'initialisation des éléments de la classe.
    def __init__(self, data):
        self.first_node = Node(data)
        self.last_node = self.first_node
        self.size = 1


    # "__str__" méthode qui permet de représenter la liste chaînée
    # sous forme de chaîne de caractères en les séparant d'un tiret "-".
    def __str__(self):
        txt = str(self.first_node.data)
        current_node = self.first_node
        while current_node.next_node is not None:
            current_node = current_node.next_node
            txt += "-" + str(current_node.data)
        return txt


    # Création d'une méthode "insert_first" qui permet l'insertion 
    # d'un nouveau nœud au début de la liste.
    def insert_first(self, data): 
        N = self.first_node 
        #Création d'une variable N qui sauvegarde la valeur de départ du premier noeud
        self.first_node = Node(data)
        self.first_node.next_node = N
        self.size += 1


    # Création d'une méthode "get_size" qui renvoie le nombre de nœuds 
    # que contient la liste chaînée.
    def get_size(self):
        return self.size


    # Création d'une méthode "append" qui permet l'ajout d'un nouveau nœud à la fin de la liste.
    # Cela en créant un nouveau nœud avec sa donnée et met à jour le premier et le dernier noeud
    # afin que ce nouveau nœud devienne le dernier nœud de la liste.
    def append(self, data):
        new_last_node = Node(data)
        self.last_node.next_node = new_last_node
        self.last_node = new_last_node
        self.size += 1


    # Création d'une méthode pop qui permet de supprimer et de renvoyer la dernière donnée 
    # (donc le last_node) de la liste.
    def pop(self):
        if self.size == 0:
            return None

        data = self.last_node.data
        if self.size == 1:
            self.first_node = None
            self.last_node = None
        else:
            current_node = self.first_node
            while current_node.next_node != self.last_node:
                current_node = current_node.next_node
            current_node.next_node = None
            self.last_node = current_node

        self.size -= 1
        return data


# Création d'une classe HistoryManager qui permet de gérer les commandes de l'historique du Bot
class HistoryManager:
    #Initialisation des éléments de la classe
    def __init__(self):
        self.history = {}
        self.history_lock = False


    # Création de la méthode "add_to_history" permet d'ajouter une nouvelle commande 
    # à l'historique d'un utilisateur choisi.
    def add_to_history(self, user, command):
        if self.history_lock:
            return "Accès refusé. L'historique est verrouillé."

        if user in self.history:
            self.history[user].append(command)
        else:
            self.history[user] = ChainedList(command)

        self.history_lock = True #Activation du verrou
        return "Commande ajoutée à l'historique."
         

    # Création de la méthode "last_command" qui renvoie la dernière commande enregistrée
    # pour un utilisateur choisi.
    def last_command(self, user):
        if user in self.history:
            return str(self.history[user].last_node.data)
        else:
            return "Aucune commande trouvée pour cet utilisateur."

    # Création de la méthode "all_commands" qui renvoie toutes les commandes enregistrées
    # pour un utilisateur choisi. 
    def all_commands(self, user):
        if user in self.history:
            return str(self.history[user])
        else:
            return "Aucune commande trouvée pour cet utilisateur."


    # Création de la méthode "navigate_history" qui permet de naviguer dans l'historique
    # des commandes d'un utilisateur choisi dans une direction choisi ("forward" ou "backward").
    def navigate_history(self, user, direction):
        if user in self.history:
            if direction == "forward":
                if self.history[user].last_node != self.history[user].first_node:
                    current_node = self.history[user].first_node.next_node
                    if current_node.next_node:
                        self.history[user].first_node = current_node
                    return str(current_node.data)
            elif direction == "backward":
                if self.history[user].last_node != self.history[user].first_node:
                    current_node = self.history[user].first_node
                    if current_node != self.history[user].last_node:
                        while current_node.next_node.next_node:
                            current_node = current_node.next_node
                        self.history[user].first_node = current_node
                    return str(current_node.data)
            else:
                return "Direction invalide."
        else:
            return "Aucune commande trouvée pour cet utilisateur."

    # Création de la méthode "clear_history" qui permet de vider l'historique des commandes
    #  pour un utilisateur choisi.
    def clear_history(self, user):
        if user in self.history:
            del self.history[user]


# Création d'un objet Intents qui représente les intentions que le bot peut recevoir de Discord
# soit toutes.
intents = discord.Intents.all() 

# Création d'une instance de la classe HistoryManager
history_manager = HistoryManager()

# Création d'un objet Bot qui représente le bot Discord lui-même ainsi qu'un prefix personnalisé. 
client = commands.Bot(command_prefix="/", intents = intents)

#Création des événements ainsi que des commandes que l'on retrouvera sur le BOT.
@client.event
async def on_ready():
    print("Le bot est prêt !") 

@client.event
async def on_member_join(member):
    general_channel = client.get_channel(977137496720826368)
    await general_channel.send("Bienvenue sur le serveur ! "+ member.name)

@client.command(name="add")
async def add_to_history(ctx, *args):
    command = ' '.join(args)
    user = ctx.author.id
    response = history_manager.add_to_history(user, command)
    await ctx.send(response)


@client.command(name="last")
async def last_command(ctx):
    user = ctx.author.id
    response = history_manager.last_command(user)
    await ctx.send(response)


@client.command(name="all")
async def all_commands(ctx):
    user = ctx.author.id
    response = history_manager.all_commands(user)
    await ctx.send(response)


@client.command(name="navigue")
async def navigate_history(ctx, direction):
    user = ctx.author.id
    response = history_manager.navigate_history(user, direction)
    await ctx.send(response)


@client.command(name="clear")
async def clear_history(ctx):
    user = ctx.author.id
    history_manager.clear_history(user)
    await ctx.send("Historique effacé pour cet utilisateur.")

@client.command(name="del")
async def delete(ctx):
    await ctx.channel.purge(limit=10)
    user = ctx.author.id
    command = "!del"
    response = history_manager.add_to_history(user, command)
    await ctx.send(response)


#Lancement du bot
client.run("MTA5MTMzNTg0MzQyMTEwMjA4MA.GTJw-z.D83j8ThR0hD70705w6R_S2iX3rjbc1JS88uhVo")

