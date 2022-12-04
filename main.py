# -- Modules --
from bs4 import BeautifulSoup
import requests
import json
from flask import Flask
import src.routes as routes

# -- Config --
collection_username = 'megtrinity'
local_file_path = f"./local/{collection_username}_collection.xml"
save_locally = True


# -- Functions --
def init():
    parsed_data = get_parsed_data()
    print(parse_items(parsed_data))


def parse_data(content, save):
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
        with open(local_file_path, 'w', encoding='UTF8') as file:
            file.write(parsed_data.prettify())
        print(f"\033[92mData saved successfully in \033[93m{local_file_path}\033[92m!\033[0m")

    return parsed_data


def get_parsed_data():
    global save_locally

    response = requests.get(routes.base_url + routes.collection_route + '/' + collection_username)

    if not response.status_code == 200:
        print(f"\033[91m{response.status_code} - Cannot connect to server.\033[0m")
        save_locally = False
        with open(local_file_path, 'r', encoding='UTF8') as file:
            response = file.read()

    else:
        print(f"\033[92m{response.status_code} - Connection to server established!\033[0m")
        print('\033[95mCollecting data...\033[0m')
        response = response.content

    return parse_data(response, save_locally)


def parse_items(data):
    print('\033[95mParsing items...\033[0m')
    parsed_items_list = []

    items_list = data.findAll('item')

    for item in items_list:
        item_id = item.get('objectid')
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


init()
