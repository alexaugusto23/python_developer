# pip install PyAutoGUI
# pip install py-trello
# pip install trello

from access import api_key_devops, api_token
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json


import requests
key = api_key_devops
token = api_token

# Creating Boards
def create_board(board_name):
    url = "https://api.trello.com/1/boards/"
    querystring = {"name": board_name, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    board_id = response.json()["shortUrl"].split("/")[-1].strip()
    return board_id

# print(create_board("teste"))

# Getting ID Boards
def getting_list_id():
    url = f"https://api.trello.com/1/boards"
    querystring = {"key": key, "token": token}
    response = requests.request("GET", url, params=querystring)
    board_id = response.text
    return board_id

print(getting_list_id())

############################################################################

# Creating Lists
def create_list(board_id, list_name):
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    querystring = {"name": list_name, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    list_id = response.json()["id"]
    return list_id

# print(create_list('OzBaszyy','teste'))

# Getting ID lists
def getting_list_id(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    querystring = {"key": key, "token": token}
    response = requests.request("GET", url, params=querystring)
    list_id = response.text
    list_id_dois = response.json()
    return list_id_dois

# print(getting_list_id('OzBaszyy'))

############################################################################
# Creating Card
def create_card(list_id, card_name):
    url = f"https://api.trello.com/1/cards"
    querystring = {"name": card_name, "idList": list_id, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id

# print(create_card('60d0a06fb0ecb7643b8b68cb','criando card trello'))

# Getting ID Cards
def getting_list_id(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    querystring = {"key": key, "token": token}
    response = requests.request("GET", url, params=querystring)
    list_id = response.text
    list_id_dois = response.json()
    return list_id_dois

# print(getting_list_id('OzBaszyy'))

############################################################################

# Creating new comment to a Card
def create_card(list_id, card_name):
    url = f"https://api.trello.com/1/cards/{id}/actions/comments"
    querystring = {'text': '{text}', "idList": list_id, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id

############################################################################

# Tasks Trello
# import os
# from trello import create_board, create_list, create_card
# board_id = create_board("Tasks")
# for filename in os.listdir():
#     if filename.endswith(".txt"):
#         filename = os.path.splitext(filename)[0]
#         list_name = create_list(board_id, filename.title())
#         with open(f"{filename}.txt", "r") as txt_file:
#             for card_name in txt_file.readlines():
#                 create_card(list_name, card_name)