import discord
from key import TOKEN
from discord.ext import commands
import requests
import random
import re
from translate import status_translations, genre_translations  # Importa as listas de traduções

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
TOKEN = TOKEN

# Defina a URL da API GraphQL da AniList
url = 'https://graphql.anilist.co'

# Defina a sua consulta GraphQL para obter um manga aleatório do gênero "Comédia"
query = '''
query ($genre: String, $perPage: Int) {
  Page(perPage: $perPage) {
    media (genre: $genre, type: MANGA, isAdult: false) {
      id
      title {
        romaji
        english
        native
      }
      status
      chapters
      volumes
      genres
      description
    }
  }
}
'''

# Defina os cabeçalhos da requisição
headers = {
    'Content-Type': 'application/json',
}

# Defina os argumentos da consulta
variables = {
    'genre': 'Comedy',
    'perPage': 50
}

@bot.event
async def on_ready():
    print(f'{bot.user} está online!')

@bot.command(name='comedia')
async def get_random_comedy_manga(ctx):
    # Faça a solicitação POST à API GraphQL
    response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'errors' in data:
            await ctx.send("Erro na resposta da API.")
        else:
            manga_list = data['data']['Page']['media']
            random_manga = random.choice(manga_list)
            
            translated_status = status_translations.get(random_manga['status'], random_manga['status'])
            
            translated_genres = [genre_translations.get(genre, genre) for genre in random_manga['genres']]
            formatted_genres = ', '.join(translated_genres)
            
            description_cleaned = random_manga['description']
            description_cleaned = re.sub(r'<[bB][rR]>', '\n', description_cleaned)
            description_cleaned = re.sub(r'<[iI]>|<\/[iI]>', '', description_cleaned)
            description_cleaned = re.sub(r'<[sS][tT][rR][oO][nN][gG]>', '**', description_cleaned)
            description_cleaned = re.sub(r'<\/[sS][tT][rR][oO][nN][gG]>', '**', description_cleaned)
            
            description_parts = [description_cleaned[i:i+400] for i in range(0, len(description_cleaned), 400)]
            description = '\n'.join(description_parts)
            
            formatted_message = (
                f"**Título (romaji):** {random_manga['title']['romaji']}\n"
                f"**Título (inglês):** {random_manga['title']['english']}\n"
                f"**Título (nativo):** {random_manga['title']['native']}\n"
                f"**Status:** {translated_status}\n"
                f"**Número de Capítulos:** {random_manga['chapters']}\n"
                f"**Número de Volumes:** {random_manga['volumes']}\n"
                f"**Gêneros:** {formatted_genres}\n"
                f"**Descrição:** {description}"
            )
            await ctx.send(formatted_message)
    else:
        await ctx.send("Erro na solicitação à API.")

# Executa o bot com o token
bot.run(TOKEN)
