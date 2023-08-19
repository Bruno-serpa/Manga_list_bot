import disnake
from disnake.ext import commands
from key import TOKEN
from api_request import perform_api_request


intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
TOKEN = TOKEN

# Definindo a URL da API GraphQL do AniList
url = 'https://graphql.anilist.co'

# Definindo a consulta GraphQL para obter um manga aleatório do gênero (LIGHT_NOVEL ou ANIME ou MANGA)
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
    activity = disnake.Activity(type=disnake.ActivityType.listening, name='Zorro do Asfalto')
    await bot.change_presence(status=disnake.Status.online, activity=activity)
    print(f'{bot.user} está online!')



#--------------------------------------------------------------- add comandos -----------------------------------------------------------------------



# /acao
@bot.slash_command(name='acao', description='Pega um mangá aleatório que contenha o gênero ação')
async def get_random_action_manga(inter):
    variables = {
        'genre': 'Action',
        'perPage': 100
    }
    formatted_message = perform_api_request(url, query, variables, headers)
    await inter.response.send_message(formatted_message)


# /aventura
@bot.slash_command(name='aventura', description='Pega um mangá aleatório que contenha o gênero aventura')
async def get_random_adventure_manga(inter):
    variables = {
        'genre': 'Adventure',
        'perPage': 100
    }
    formatted_message = perform_api_request(url, query, variables, headers)
    await inter.response.send_message(formatted_message)


#--------------------------------------------------------------- fim dos comandos -----------------------------------------------------------------------

# Executa o bot com o token
bot.run(TOKEN)
