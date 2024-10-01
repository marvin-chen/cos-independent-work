import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_pokemon_stats():
    url = 'https://pokemondb.net/pokedex/all'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', id='pokedex')
    
    pokemon_data = []
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        if len(cells) >= 10:
            pokemon_data.append({
                'Number': cells[0].text.strip(),
                'Name': cells[1].find('a', class_='ent-name').text.strip(),
                'Type': ' '.join([t.text for t in cells[2].find_all('a')]),
                'Total': int(cells[3].text.strip()),
                'HP': int(cells[4].text.strip()),
                'Attack': int(cells[5].text.strip()),
                'Defense': int(cells[6].text.strip()),
                'Sp. Atk': int(cells[7].text.strip()),
                'Sp. Def': int(cells[8].text.strip()),
                'Speed': int(cells[9].text.strip())
            })
    return pd.DataFrame(pokemon_data)

def get_pokemon_images_and_generations():
    url = 'https://pokemondb.net/pokedex/national'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    pokemon_data = {}
    current_gen = 1
    for element in soup.find_all(['h2', 'div']):
        if element.name == 'h2' and 'Generation' in element.text:
            current_gen = int(element.text.split()[1])
        elif element.name == 'div' and 'class' in element.attrs and 'infocard-list' in element['class']:
            for card in element.find_all('div', class_='infocard'):
                number_elem = card.find('small')
                img_elem = card.find('img')
                if number_elem and img_elem:
                    number = number_elem.text.strip()[1:]  # Remove the '#' symbol
                    img_url = img_elem['src']
                    pokemon_data[number] = {'Generation': current_gen, 'Image URL': img_url}
    
    return pokemon_data

def get_pokemon_height_weight(name):
    url = f'https://pokemondb.net/pokedex/{name.lower()}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    vitals_table = soup.find('table', class_='vitals-table')
    height = 'Unknown'
    weight = 'Unknown'
    
    if vitals_table:
        for row in vitals_table.find_all('tr'):
            header = row.find('th').text.strip()
            if header == 'Height':
                height = row.find('td').text.split()[0]  # Get the first value
            elif header == 'Weight':
                weight = row.find('td').text.split()[0]  # Get the first value
    
    return height, weight

def main():
    print("Fetching Pokemon stats...")
    stats_df = get_pokemon_stats()
    
    print("Fetching Pokemon images and generations...")
    images_and_gens = get_pokemon_images_and_generations()
    
    print("Fetching height and weight for each Pokemon...")
    for index, row in stats_df.iterrows():
        number = row['Number']
        name = row['Name']
        if number in images_and_gens:
            stats_df.at[index, 'Generation'] = images_and_gens[number]['Generation']
            stats_df.at[index, 'Image URL'] = images_and_gens[number]['Image URL']
        
        height, weight = get_pokemon_height_weight(name)
        stats_df.at[index, 'Height'] = height
        stats_df.at[index, 'Weight'] = weight
        
        print(f"Processed {name}")
        time.sleep(1)  # Be respectful to the server
    
        if index % 50 == 0:  # Save every 50 Pokémon
            stats_df.to_csv('pokemon_data_intermediate.csv', index=False)
            print(f"Saved intermediate results after processing {index} Pokémon")
    
    print("Saving data to CSV...")
    stats_df.to_csv('pokemon_complete_data.csv', index=False)
    print("Done!")

if __name__ == "__main__":
    main()