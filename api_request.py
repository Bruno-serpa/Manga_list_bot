import requests
import random
import re
from translate import status_translations, genre_translations

def perform_api_request(url, query, variables, headers):
    response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'errors' in data:
            return "Erro na resposta da API."
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
                f"**Nota:** {random_manga['averageScore']}/100\n"
                f"**Número de Capítulos:** {random_manga['chapters']}\n"
                f"**Número de Volumes:** {random_manga['volumes']}\n"
                f"**Gêneros:** {formatted_genres}\n"
                f"**Descrição:** {description}\n"
                f"\n**Link para Ler:** {random_manga['siteUrl']}"
            )
            return formatted_message
    else:
        return "Erro na solicitação à API."
