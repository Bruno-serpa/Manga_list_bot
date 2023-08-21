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
            description_cleaned = re.sub(r'<[bB]>|<\/[bB]>', '**', description_cleaned)
            description_cleaned = re.sub(r'<[sS][tT][rR][oO][nN][gG]>', '**', description_cleaned)
            description_cleaned = re.sub(r'<\/[sS][tT][rR][oO][nN][gG]>', '**', description_cleaned)

            description_parts = [description_cleaned[i:i+400] for i in range(0, len(description_cleaned), 400)]
            description = '\n'.join(description_parts)

            # Condição para a nota
            if random_manga['averageScore'] is None or random_manga['averageScore'] == 'None':
                formatted_note = 'Sem nota'
            else:
                formatted_note = f"{random_manga['averageScore']}/100"
            
            # Condição para o nome em ingles
            if random_manga['title']['english'] is None or random_manga['title']['english'] == 'None':
                formatted_name_english = random_manga['title']['romaji']
            else:
                formatted_name_english = random_manga['title']['english']
                
            # Condição para o números de capitulos
            if random_manga['chapters'] is None or random_manga['chapters'] == 'None':
                formatted_chapter_number = 'Indisponível'
            else:
                formatted_chapter_number = random_manga['chapters']
                
            # Condição para o números de capitulos
            if random_manga['volumes'] is None or random_manga['volumes'] == 'None':
                formatted_volum_number = 'Indisponível'
            else:
                formatted_volum_number = random_manga['volumes']

            formatted_message = (
                f"**Título (romaji):** {random_manga['title']['romaji']}\n"
                f"**Título (inglês):** {formatted_name_english}\n"
                f"**Título (nativo):** {random_manga['title']['native']}\n"
                f"**Status:** {translated_status}\n"
                f"**Nota:** {formatted_note}\n"
                f"**Número de Capítulos:** {formatted_chapter_number}\n"
                f"**Número de Volumes:** {formatted_volum_number}\n"
                f"**Gêneros:** {formatted_genres}\n"
                f"**Descrição:** {description}\n"
                f"\n**Link para Ler:** {random_manga['siteUrl']}"
            )

            return formatted_message
    else:
        return "Erro na solicitação à API."