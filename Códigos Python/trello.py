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
    url = "https://api.trello.com/1/boards"
    querystring = {"name": board_name, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    board_id = response.json()["shortUrl"].split("/")[-1].strip()
    return board_id

# print(create_board("teste"))

# Getting a Member data
def getting_member(id):
    url = f"https://api.trello.com/1/members/{id}"
    querystring = {"key": key, "token": token}
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    member_id = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    return member_id

# print(getting_member("alexsandroaugustoignacio1"))

# Gettings Boards
def getting_boards_id(id):
    url = f"https://api.trello.com/1/members/{id}/boards"
    querystring = {"key": key, "token": token}
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    board_id = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    return board_id

# print(getting_boards_id("60458b714f92b01f2b514382"))

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

# print(getting_list_id('PnwdOH2A'))

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
def getting_cards_id(board_id, list_id):
    url = f"https://api.trello.com/1/lists/{list_id}/cards"
    querystring = {"key": key, "token": token}
    response = requests.request("GET", url, params=querystring)
    cards = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    return cards

# print(getting_cards_id('PnwdOH2A','60c8eaac5057396be2a66ac2'))

# Getting ID Cards
def getting_cards_values(card_id):
    url = f"https://api.trello.com/1/cards/{card_id}"
    querystring = {"key": key, "token": token}
    response = requests.request("GET", url, params=querystring)
    cards_values = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    return cards_values

# print(getting_cards_values('Cf485Bzj'))

############################################################################

# Creating new comment to a Card
def create_comment(id_card, text):
    url = f"https://api.trello.com/1/cards/{id_card}/actions/comments"
    querystring = {'text': f'{text}', "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    comment = response.json()["id"]
    return comment

# print(create_comment('Cf485Bzj',"trello teste"))

# Getting ID Comments
def getting_comments_id( card_id ):
    url = f"https://api.trello.com/1/cards/{card_id}/actions"
    querystring = {"key": key, "token": token}
    response = requests.request("GET", url, params=querystring)
    comments_id = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    return comments_id

result = json.loads(getting_comments_id('Cf485Bzj'))

# print(result[0]['data']['text'])

# for i in result:
#    print(i['text']['id']['date'])
#    # print(f"{i['id']} + {i['text']}")
# # # print(result[1]["id"])

for i in result:
   print(f"{'#'*30}\n{i['memberCreator']['fullName']}\n{i['id']}\n\n{i['data']['text']}\n{'#'*30}\n\n")

def delete_comment(id_card, idAction):
    url = f"https://api.trello.com/1/cards/{id_card}/actions/{idAction}/comments"
    querystring = {"key": key, "token": token}
    response = requests.request("DELETE", url, params=querystring)
    return response.text

# print(delete_comment('Cf485Bzj',"60d0dc5df42d9625d3fa331c"))

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