# -- Modules --
import os
import re
from bs4 import BeautifulSoup
import requests
import json
from flask import Flask
import src.routes as routes

# -- Config --
collection_username = 'megtrinity'
local_collection_file_path = f"./local/collection/{collection_username}.xml"
local_boardgame_file_path = './local/boardgame'
save_locally = True
app = Flask(__name__)


# -- Functions --
def init():
    if not os.path.isdir("./local/collection"):
        os.makedirs("./local/collection")
    if not os.path.isdir("./local/boardgame"):
        os.makedirs("./local/boardgame")


def parse_data(content, save, game_id):
    print('\033[95mParsing data...\033[0m')

    parsed_data = BeautifulSoup(content, features='xml')

    have_error = parsed_data.find('error')

    if have_error:
        error_message = parsed_data.find('message').string
        print(f"\033[91mAn error occurred:\033[93m {error_message}\033[0m")
        exit()

    print('\033[92mData parsed successfully with no error!\033[0m')

    if save:
        print('\033[95mSaving data...\033[0m')
        file_path = f"{local_boardgame_file_path}/{game_id}.xml" if game_id else local_collection_file_path
        with open(file_path, 'w', encoding='UTF8') as file:
            file.write(parsed_data.prettify())
        print(f"\033[92mData saved successfully in \033[93m{file_path}\033[92m!\033[0m")

    return parsed_data


def get_parsed_data(route, game_id=None):
    global save_locally

    response = requests.get(route)

    if not response.status_code == 200:
        print(f"\033[91m{response.status_code} - Cannot connect to server.\033[0m")
        save_locally = False
        with open(f"{local_boardgame_file_path}/{game_id}.xml" if game_id else local_collection_file_path, 'r',
                  encoding='UTF8') as file:
            response = file.read()

    else:
        print(f"\033[92m{response.status_code} - Connection to server established!\033[0m")
        print('\033[95mCollecting data...\033[0m')
        response = response.content

    return parse_data(response, save_locally, game_id)


def parse_items_in_collection(data):
    print('\033[95mParsing items...\033[0m')
    parsed_items_list = []

    items_list = data.findAll('item')

    for item in items_list:
        item_id = int(item.get('objectid'))
        item_title = item.find('name').string if item.find('name') else False
        item_lst_published_year = int(item.find('yearpublished').string) if item.find('yearpublished') else False
        item_stats = item.find('stats')
        item_min_player = int(item_stats.get('minplayers')) if item_stats.get('minplayers') else False
        item_max_player = int(item_stats.get('maxplayers')) if item_stats.get('maxplayers') else False
        item_min_playtime = int(item_stats.get('minplaytime')) if item_stats.get('minplaytime') else False
        item_max_playtime = int(item_stats.get('maxplaytime')) if item_stats.get('maxplaytime') else False
        item_thumbnail = item.find('thumbnail').string if item.find('thumbnail') else False

        item_dict = {
            'id': item_id,
            'title': item_title,
            'lst_published_year': item_lst_published_year,
            'players': item_max_player if item_max_player == item_min_player else f"{item_min_player} - {item_max_player}",
            'playtime': item_max_playtime if item_max_playtime == item_min_playtime else f"{item_min_playtime} - {item_max_playtime}",
            'thumbnail': item_thumbnail
        }

        parsed_items_list.append(item_dict)

    return parsed_items_list


def parse_game_item(data):
    print('\033[95mParsing items...\033[0m')

    game = data.find('boardgame')
    game_id = int(game.get('objectid'))
    game_names = game.findAll('name')
    game_names_list = []
    game_description = game.find('description').string if game.find('description') else False
    game_image = game.find('image').string if game.find('image').string else False
    game_min_player = int(game.find('minplayers').string) if game.find('minplayers') else False
    game_max_player = int(game.find('maxplayers').string) if game.find('maxplayers') else False
    game_min_playtime = int(game.find('minplaytime').string) if game.find('minplaytime') else False
    game_max_playtime = int(game.find('maxplaytime').string) if game.find('maxplaytime') else False
    game_categories = game.findAll('boardgamecategory')
    game_categories_list = []
    game_expansions = game.findAll('boardgameexpansion')
    game_expansions_list = []

    for game_name in game_names:
        game_names_list.append(game_name.string)

    for game_categorie in game_categories:
        game_categories_list.append(game_categorie.string)

    for game_expansion in game_expansions:
        game_expansions_list.append(game_expansion.string)

    game_dict = {
        'id': game_id,
        'title': game_names_list,
        'description': strip_html(game_description),
        'image': game_image,
        'players': game_max_player if game_max_player == game_min_player else f"{game_min_player} - {game_max_player}",
        'playtime': game_max_playtime if game_max_playtime == game_min_playtime else f"{game_min_playtime} - {game_max_playtime}",
        'categories': list_to_string(game_categories_list),
        'expansions': game_expansions_list
    }

    return game_dict


def strip_html(html):
    text = re.compile(r'<.*?>')
    return text.sub('', html)


def list_to_string(current_list, delimiter=','):
    temp = list(map(str, current_list))
    return delimiter.join(temp)


init()


# -- API Routes --
@app.route('/')
def home():
    return json.dumps({
        'routes': {
            f"{collection_username}'s boardgame collection": '/games',
            'Search game by id': '/games/[:id]'
        }
    })


@app.route('/games')
def get_games():
    route = routes.base_url + routes.collection_route + '/' + collection_username
    parsed_data = get_parsed_data(route)
    return json.dumps(parse_items_in_collection(parsed_data))


@app.route('/games/<int:game_id>')
def get_games_by_id(game_id):
    route = routes.base_url + routes.boardgame_route + f"/{game_id}"
    parsed_data = get_parsed_data(route, game_id)
    return json.dumps(parse_game_item(parsed_data))
