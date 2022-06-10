# print("***** Welcome to Spotify search. Search for an artist and get their top tracks! *****")
# name=input("Enter artist name: ")
# #get the artist from name
# print("These are the top 3 search results: ")
# # a loop for displaying names
# print("\n")
# choice=input("Pick an artist number to get their top 3 tracks: ")
# #get the tracks on basis of choice
# print("These are the top 3 tracks of ",name,":")
# #get the tracks 
# print("\n")
# print("Hope you enjoy the tracks!")

from pip._vendor import requests


CLIENT_ID = "68d5a57e4a974a3cb88d361a27ec5280"
CLIENT_SECRET = "edd9003849f54e8f8c172329a60aaf0e"
BASE_URL = 'https://api.spotify.com/v1/'

#Save the access token
access_token = 'BQBLeoS8WZy36_6owutGn6iaeaDCSRBtGcLGqLSSC7FPcpdsGObW0-v-zVGrFhSWNt3PqVQTu5q6ElEU-Mq2v7N9rAHteLY8bUdwQ_GAnHnifZ0EwF2d8guN0KcwfyyavsRVHz7ozZvR4LRP_kVjk4_yyJVL9-mwgilynGQvAd8d0ouxQvF7rRl0XYDJw6eIX8DB'

#Need to pass access token into header to send properly formed GET request to API server
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

r = requests.get(BASE_URL + 'search?q=tania%20bowra&type=artist', headers=headers)
r = r.json()

print(r)