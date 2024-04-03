import tweepy

# Remplacez 'YOUR_API_KEY', 'YOUR_API_SECRET_KEY', 'YOUR_ACCESS_TOKEN', 'YOUR_ACCESS_TOKEN_SECRET' par vos propres clés et jetons d'accès Twitter
api_key = 'fqbeUl5lZOIJyrZk0v29WHCHr'
api_secret_key = 'cXH0kc3eTt3VJOgF4bhQ6bkS7SR0ioSAmwXieoJOGfkIv5ymt9'
access_token = '1237665439674662912-xRmUcPdmYcUjUon2dGU2qPBCbONUNi'
access_token_secret = 'qo5vsljteVicP4Y6oEe2JPtMAcatHgHj8E1f6f9waBSft'

# Authentification avec les clés et jetons d'accès Twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

# Création d'un objet API Twitter
api = tweepy.API(auth)

# Récupération de la liste d'amis (utilisateurs suivis) de votre compte Twitter
friends = api.friends()

# Affichage des noms d'utilisateur des amis
for friend in friends:
    print(friend.screen_name)