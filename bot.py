import discord
from key import TOKEN
from discord.ext import commands
from api_request import perform_api_request

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
TOKEN = TOKEN

# Definindo a URL da API GraphQL do AniList
url = 'https://graphql.anilist.co'

# Definindo a consulta GraphQL para obter um manga aleatório do gênero
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
      averageScore
      siteUrl
    }
  }
}
'''


# Definindo os cabeçalhos da requisição
headers = {
    'Content-Type': 'application/json',
}

# Verificando se o bot tá online
@bot.event
async def on_ready():
    print(f'{bot.user} está online!')



#--------------------------------------------------------------- add comandos -----------------------------------------------------------------------



# /acao
@bot.command(name='acao')
async def action_command(ctx):
    variables = {
        'genre': 'Action',
        'perPage': 50
    }
    formatted_message = perform_api_request(url, query, variables, headers)
    await ctx.send(formatted_message)


# /aventura
@bot.command(name='aventura')
async def get_random_action_manga(ctx):
    variables = {
        'genre': 'Adventure',
        'perPage': 50
    }
    formatted_message = perform_api_request(url, query, variables, headers)
    await ctx.send(formatted_message)
    
       
# /comedia
@bot.command(name='comedia')
async def get_random_comedy_manga(ctx):
    
    variables = {
        'genre': 'Comedy',
        'perPage': 50
    }
    formatted_message = perform_api_request(url, query, variables, headers)
    await ctx.send(formatted_message)


# /drama
@bot.command(name='drama')
async def get_random_comedy_manga(ctx):
    
    variables = {
        'genre': 'Drama',
        'perPage': 50
    }
    formatted_message = perform_api_request(url, query, variables, headers)
    await ctx.send(formatted_message)

# Executa o bot com o token
bot.run(TOKEN)
