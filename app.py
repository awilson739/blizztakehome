import requests
import configparser
import json
import random
import requests_oauthlib
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from flask import Flask, render_template

config = configparser.ConfigParser()
config.read('config')
app = Flask(__name__)
def get_token():
    client = BackendApplicationClient(client_id=config['default']['client_id'])
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url='https://us.battle.net/oauth/token',client_id=config['default']['client_id'],client_secret=config['default']['client_secret'])
    return token['access_token']

def get_cards():
    access_token = get_token()
    druid = requests.get(f'https://us.api.blizzard.com/hearthstone/cards?locale=en_US&class=druid&rarity=legendary&sort=Name&access_token={access_token}')
    warlock = requests.get(f'https://us.api.blizzard.com/hearthstone/cards?locale=en_US&class=warlock&rarity=legendary&access_token={access_token}')
    cards = {}
    cards['cards'] = warlock.json()['cards'] + druid.json()['cards']
    return cards

def organize_cards(cards):
    new_cards = {}
    deck = {}
    for card in cards['cards']:
        new_cards.setdefault('cards',[])
        if card['manaCost'] >= 7:
            new_cards['cards'].append(card)
    random.shuffle(new_cards['cards'])
    deck.setdefault('cards',[])
    deck['cards'].append(random.choices(new_cards['cards'],k=10))
    return deck

@app.route('/')   
def create_table():
    access_token = get_token()
    metadata_sets = requests.get(f'https://us.api.blizzard.com/hearthstone/metadata/sets?locale=en_US&access_token={access_token}')
    metadata_class = requests.get(f'https://us.api.blizzard.com/hearthstone/metadata/classes?locale=en_US&access_token={access_token}')
    metadata_type = requests.get(f'https://us.api.blizzard.com/hearthstone/metadata/types?locale=en_US&access_token={access_token}')

    cards = organize_cards(get_cards())
    return render_template('cards.html',metadata_sets=metadata_sets.json(),metadata_classes=metadata_class.json(),new_cards=cards['cards'],metadata_type=metadata_type.json())



if __name__ == '__main__':
    app.run()