import tweepy, argparse, os

# variáveis de ambiente pra autentificação 
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

# Inicializando o parse
parser = argparse.ArgumentParser(
description="simple script to demonstrate argparse usage"
)

# Adicionando um parâmetro posicional 
parser.add_argument('printme', help="The string to be printed")

# Fazendo parse dos argumentos
arguments = parser.parse_args()

# Imprimindo a String 
print(arguments.printme)

# Acessando, enviando e recebendo response
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
response = api.update_status(arguments.printme)
print('Status posted', response)

# como rodar essa bagaça no terminal: 
# CONSUMER_KEY=etcetc python3 nome_arquivo.py "hello world"
