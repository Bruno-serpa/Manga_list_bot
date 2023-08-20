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
headers = {
    'Content-Type': 'application/json',
}

# Verificando se o bot tá online e adicionando status de musica
@bot.event
async def on_ready():
    activity = disnake.Activity(type=disnake.ActivityType.listening, name='Zorro do Asfalto')
    await bot.change_presence(status=disnake.Status.online, activity=activity)
    print(f'{bot.user} está online!')

class Select(disnake.ui.Select):
    def __init__(self):
        options=[
            disnake.SelectOption(label="Ação", description="Pega um mangá aleatório que contenha o gênero ação", value="acao"),
            disnake.SelectOption(label="Aventura", description="Pega um mangá aleatório que contenha o gênero aventura", value="aventura"),
        ]
        super().__init__(placeholder="Escolha um gênero", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: disnake.Interaction):
      
#--------------------------------------------------------------- add comandos -----------------------------------------------------------------------

        if self.values[0] == "acao":
            variables = {
                'genre': 'Action',
                'perPage': 100
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)
        elif self.values[0] == "aventura":
            variables = {
                'genre': 'Adventure',
                'perPage': 100
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)

#--------------------------------------------------------------- fim dos comandos -----------------------------------------------------------------------

class SelectView(disnake.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=timeout)
        self.add_item(Select())

@bot.slash_command(name='menu', description='Pega um mangá aleatório pelo gênero')
async def menu(ctx):
    await ctx.response.send_message("Escolha um gênero:", view=SelectView())

bot.run(TOKEN)