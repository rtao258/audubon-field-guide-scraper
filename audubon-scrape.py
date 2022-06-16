import logging
import requests
from bs4 import BeautifulSoup

with open('audubon.html', 'r') as html:
    html_doc = html.read()

soup = BeautifulSoup(html_doc, 'html.parser')

bird_grid = soup.find(class_='bird-card-grid-container')

birds = []

for bird_cell in bird_grid.find_all('div', recursive=False):

    logging.info('\n' + str(len(birds) + 1))

    bird_card = bird_cell.find('article')

    if bird_card is None:
        continue

    common_name = bird_card.find(class_='common-name').a.text.strip()
    logging.info(common_name)

    scientific_name = bird_card.find(class_='scientific-name').span.text.strip()
    logging.info(scientific_name)

    photo = bird_card.find('img')['src']
    logging.info(photo)
    with open(common_name + '.jpg', 'wb') as image_file:
        image_file.write(requests.get(image).content)
    photo_html = f'<img src="{common_name}.jpg">'

    sound_elem = bird_card.find('audio')
    if sound_elem is not None:
        sound = sound_elem['src']
        logging.info(sound)
        with open(common_name + '.mp3', 'wb') as sound_file:
            sound_file.write(requests.get(sound).content)
        sound_html = f'[sound:{common_name}.mp3]'
    else:
        logging.info('no sound')
        sound_html = ''

    birds.append('; '.join([common_name, scientific_name, photo_html, sound_html]))

with open('birds.txt', 'w') as text_file:
    for bird in birds:
        text_file.write(bird + '\n')
