######################################## Consigne ##########################################
"""
3 - (4 points) - Via un arbre binaire ou non, créer un système de discution permettant de faire un questionnaire à l'utilisateur. L'utilisateur pourra appeler une commande "help" permettant de 
lancer la conversation et le bot tentera de définir son besoin en lui posant une série de questions prédéfinies, à la fin de la conversation une réponse sera donné au besoin. 
les sujets que devra aborder sont libre.
    De plus la gestion des discutions avec le bot doit avoir un certain nombre de commandes :
    - "reset" : permettra de recommencer la discution
    - "speak about X" : permettra de savoir si un sujet est traité par le bot ou non (exemple : speak about python dira si oui ou non le bot parle de python)
"""

#CE CODE A ETE FAIT A L'AIDE DU CODE DU PROF

# Import des modules nécessaires pour utiliser la bibliothèque Discord et ses extensions.
import discord
from discord.ext import commands

# Cration d'une classe Question qui représente les question à poser à l'utilisateur. 
# Elle possède des pré-réponses : "oui", "non"
class Question:
    def __init__(self, text):
        self.text = text
        self.yes = None
        self.no = None

# Création d'un objet Intents qui représente les intentions que le bot peut recevoir de Discord
# soit toutes.
intents = discord.Intents.all() 

# Création d'un objet Bot qui représente le bot Discord lui-même ainsi qu'un prefix personnalisé.
bot = commands.Bot(command_prefix="/", intents=intents)

# Création d'une classe Conversation pour gérer les conversations des utilisateurs.
class Conversation:
    def __init__(self):
        self.conversations = {}

    # Création d'une méthode "get_conversation_history" qui permet de récupérer 
    # l'historique de conversation d'un utilisateur choisi par son ID.
    def get_conversation_history(self, user_id):
        if user_id in self.conversations:
            return self.conversations[user_id]
        else:
            return None

    # Création d'une méthode "update_conversation_history" qui permet de rmettre à jour 
    # l'historique de conversation d'un utilisateur choisi par son ID.
    def update_conversation_history(self, user_id, command):
        if user_id in self.conversations:
            self.conversations[user_id].append(command)
        else:
            self.conversations[user_id] = [command]

# Création d'une instance de la classe Conversation
conversation = Conversation()

#Création des événements ainsi que des commandes que l'on retrouvera sur le BOT.
@bot.event
async def on_ready():
    print("Le bot est prêt !") 

@bot.event
async def on_member_join(member):
    general_channel = bot.get_channel(977137496720826368)
    await general_channel.send("Bienvenue sur le serveur ! "+ member.name)


@bot.command(name="start_conversation")
async def start_conversation(ctx):
    user_id = str(ctx.message.author.id)
    
    # Récupérer l'historique de conversation de l'utilisateur s'il existe
    conversation_history = conversation.get_conversation_history(user_id)
    if conversation_history:
        conversation_history.append("Conversation déjà en cours.")
    else:
        conversation_history = []
        root_question = Question("Salut, tu vas bien?")
        root_question.yes = Question("Tu passes une bonne journée?")
        root_question.no = Question("Est-ce que je peux faire quelque chose?")
        root_question_no = Question("Est-ce que vous voulez que je vous recommande quelque chose pour vous détendre?")
        root_question_no.yes = Question("Est-ce que vous aimez faire de l'exercice physique?")
        root_question_no.no = Question("Est-ce que vous aimez lire des livres ou regarder des films?")
        root_question_no_yes = Question("Super! Quel genre de livres/films aimez-vous?")
        root_question_no_no = Question("Est-ce que vous avez déjà essayé la méditation ou la respiration profonde?")
        await ask_question(ctx, root_question, conversation_history)
    
    # Mettre à jour l'historique de conversation de l'utilisateur
    conversation.update_conversation_history(user_id, conversation_history)

async def ask_question(ctx, question, conversation_history):
    await ctx.send(question.text)
    response = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    response = response.content
    conversation_history.append(response)

    if question.yes is None and question.no is None:
        conversation_history.append("Je ne sais pas quoi répondre.")
    elif question.yes is not None and response.lower().startswith('oui'):
        await ask_question(ctx, question.yes, conversation_history)
    elif question.no is not None and response.lower().startswith('non'):
        await ask_question(ctx, question.no, conversation_history)
    else:
        conversation_history.append("Je n'ai pas compris votre réponse.")

@bot.command(name="conversation_history")
async def conversation_history(ctx):
    user_id = str(ctx.message.author.id)
    
    # Récupérer l'historique de conversation de l'utilisateur
    conversation_history = conversation.get_conversation_history(user_id)
    if conversation_history:
        response_text = "\n".join(conversation_history)
    else:
        response_text = "Aucune conversation trouvée."
        await ctx.send(response_text)

@bot.command(name="reset")
async def reset_conversation(ctx):
    user_id = str(ctx.message.author.id)
    
    # Réinitialiser l'historique de conversation de l'utilisateur
    conversation.update_conversation_history(user_id, [])
    await ctx.send("La conversation a été réinitialisée.")

@bot.command(name="speak_about")
async def speak_about_topic(ctx, topic):
    # Vérifier si le bot parle du sujet spécifié
    # (vous pouvez personnaliser cette fonctionnalité avec vos propres sujets)
    available_topics = ["python", "bien-être", "lecture", "films"]
    if topic.lower() in available_topics:
        response = f"Oui, je peux parler de {topic}."
    else:
        response = f"Désolé, je ne peux pas parler de {topic}."
    await ctx.send(response)

#Lancement du bot
bot.run("MTA5MTMzNTg0MzQyMTEwMjA4MA.GTJw-z.D83j8ThR0hD70705w6R_S2iX3rjbc1JS88uhVo")
