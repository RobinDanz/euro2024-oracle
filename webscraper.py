import requests
from bs4 import BeautifulSoup
import re
import json

groups = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J'
]

if __name__ == '__main__':
    final_data = {}
    for group in groups:
        final_data[group] = []
        url = f'https://en.wikipedia.org/wiki/UEFA_Euro_2024_qualifying_Group_{group}'

        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        tags = soup.findAll('div', id=re.compile('_v_'))

        score_tables = []

        for tag in tags:
            score_tables.append(tag.findChild('table').find('tbody'))


        for result in score_tables:
            home_team = result.find('th', class_="fhome").find('a').text
            score_split = result.find('th', class_="fscore").text.split('–')
            score_home = score_split[0]
            score_away = score_split[1]

            away_team = result.find('th', class_="faway").find('a').text

            final_data[group].append(
                {
                    'home_team': home_team, 
                    'score_home': score_home, 
                    'score_away': score_away, 
                    'away_team': away_team
                }
            )

    with open('data.json', 'w') as output_file:
        json.dump(final_data, output_file)






    