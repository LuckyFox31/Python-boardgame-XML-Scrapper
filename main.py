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

    parsed_data = parse_data(response, save_locally)


get_parsed_data()
