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
    activity = disnake.Activity(type=disnake.ActivityType.listening, name='Mina do Condomínio')
    await bot.change_presence(status=disnake.Status.online, activity=activity)
    print(f'{bot.user} está online!')

#--------------------------------------------------------------- add opções -----------------------------------------------------------------------

class Select(disnake.ui.Select):
    def __init__(self):
        options = [
            disnake.SelectOption(label="Ação", description="Pega um mangá aleatório que contenha o gênero ação", value="acao"),
            disnake.SelectOption(label="Aventura", description="Pega um mangá aleatório que contenha o gênero aventura", value="aventura"),
            disnake.SelectOption(label="Comédia", description="Pega um mangá aleatório que contenha o gênero comédia", value="comedia"),
            disnake.SelectOption(label="Drama", description="Pega um mangá aleatório que contenha o gênero drama", value="drama"),
            disnake.SelectOption(label="Ecchi", description="Pega um mangá aleatório que contenha o gênero ecchi", value="ecchi"),
            disnake.SelectOption(label="Esportes", description="Pega um mangá aleatório que contenha o gênero esportes", value="esportes"),
            disnake.SelectOption(label="Ficção Científica", description="Pega um mangá aleatório que contenha o gênero ficção científica", value="ficcao_cientifica"),
            disnake.SelectOption(label="Fantasia", description="Pega um mangá aleatório que contenha o gênero fantasia", value="fantasia"),
            disnake.SelectOption(label="Mahou Shoujo", description="Pega um mangá aleatório que contenha o gênero mahou shoujo", value="mahou_shoujo"),
            disnake.SelectOption(label="Mecha", description="Pega um mangá aleatório que contenha o gênero mecha", value="mecha"),
            disnake.SelectOption(label="Mistério", description="Pega um mangá aleatório que contenha o gênero mistério", value="misterio"),
            disnake.SelectOption(label="Música", description="Pega um mangá aleatório que contenha o gênero música", value="musica"),
            disnake.SelectOption(label="Psicológico", description="Pega um mangá aleatório que contenha o gênero psicológico", value="psicologico"),
            disnake.SelectOption(label="Romance", description="Pega um mangá aleatório que contenha o gênero romance", value="romance"),
            disnake.SelectOption(label="Slice of Life", description="Pega um mangá aleatório que contenha o gênero slice of life", value="slice_of_life"),
            disnake.SelectOption(label="Sobrenatural", description="Pega um mangá aleatório que contenha o gênero sobrenatural", value="sobrenatural"),
            disnake.SelectOption(label="Suspense", description="Pega um mangá aleatório que contenha o gênero suspense", value="suspense"),
            disnake.SelectOption(label="Terror", description="Pega um mangá aleatório que contenha o gênero terror", value="terror"),
        ]


        super().__init__(placeholder="Escolher gênero", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: disnake.Interaction):
      
#--------------------------------------------------------------- add interações -----------------------------------------------------------------------

        # Ação:
        if self.values[0] == "acao":
            variables = {
                'genre': 'Action',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)

        # Aventura:
        if self.values[0] == "aventura":
            variables = {
                'genre': 'Adventure',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)

        # Comédia:
        if self.values[0] == "comedia":
            variables = {
                'genre': 'Comedy',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)

        # Drama:
        if self.values[0] == "drama":
            variables = {
                'genre': 'Drama',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)

        # Ecchi:
        if self.values[0] == "ecchi":
            variables = {
                'genre': 'Ecchi',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)

        # Esportes:
        if self.values[0] == "esportes":
            variables = {
                'genre': 'Sports',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)

        # Ficção Científica:
        if self.values[0] == "ficcao_cientifica":
            variables = {
                'genre': 'Sci-Fi',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)
            
        # Fantasia:
        if self.values[0] == "fantasia":
            variables = {
                'genre': 'Fantasy',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)

        # Mahou Shoujo:
        if self.values[0] == "mahou_shoujo":
            variables = {
                'genre': 'Mahou Shoujo',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)
            
        # Mecha:
        if self.values[0] == "mecha":
            variables = {
                'genre': 'Mecha',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)

        # Mistério:
        if self.values[0] == "misterio":
            variables = {
                'genre': 'Mystery',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)

        # Música:
        if self.values[0] == "musica":
            variables = {
                'genre': 'Music',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)

        # Psicológico:
        if self.values[0] == "psicologico":
            variables = {
                'genre': 'Psychological',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)

        # Romance:
        if self.values[0] == "romance":
            variables = {
                'genre': 'Romance',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)
            
        # Slice of Life:
        if self.values[0] == "slice_of_life":
            variables = {
                'genre': 'Slice of Life',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)

        # Sobrenatural:
        if self.values[0] == "sobrenatural":
            variables = {
                'genre': 'Supernatural',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)

        # Suspense:
        if self.values[0] == "suspense":
            variables = {
                'genre': 'Thriller',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)
            
        # Terror:
        if self.values[0] == "terror":
            variables = {
                'genre': 'Horror',
                'perPage': 1000000
            }
            formatted_message = perform_api_request(url, query, variables, headers)
            await interaction.response.send_message(formatted_message, ephemeral=False)

#--------------------------------------------------------------- add comandos -----------------------------------------------------------------------

class SelectView(disnake.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=timeout)
        self.add_item(Select())

# Comando /genero
@bot.slash_command(name='genero', description='Pega um mangá aleatório pelo gênero')
async def genero(ctx):
    await ctx.response.send_message("Bem-vindo(a) ao **Mangá List**.\nEscolha um gênero para recomendarmos um mangá aleatório", view=SelectView(), ephemeral=True)


# Comando /help
@bot.slash_command(name='help', description='Explica como o bot funciona')
async def help_command(ctx):
    help_message = (
        "📚 **Ajuda do Bot Mangá List** 📚\n\n"
        "Este bot pode recomendar mangás aleatórios com base em diferentes gêneros. Para usar o bot, siga estes passos:\n\n"
        "1. Use o comando `/genero` para escolher um gênero no menu suspenso.\n"
        "2. O bot responderá com uma recomendação de mangá aleatório do gênero selecionado.\n\n"
        "Gêneros disponíveis:\n"
        "• Ação\n• Aventura\n• Comédia\n• Drama\n• Ecchi\n• ... (outros gêneros)\n\n"
        "Observe que as recomendações são baseadas na API do AniList e podem não corresponder perfeitamente às suas preferências.\n\n"
        "Divirta-se descobrindo novos mangás!"
    )
    await ctx.response.send_message(help_message, ephemeral=True)

bot.run(TOKEN)