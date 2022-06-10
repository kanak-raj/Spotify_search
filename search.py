from pip._vendor import requests
import json

print("***** Welcome to Spotify search. Search for an artist and get their top tracks! *****")
name=input("Enter artist name: ")
CLIENT_ID = "68d5a57e4a974a3cb88d361a27ec5280"
CLIENT_SECRET = "edd9003849f54e8f8c172329a60aaf0e"
BASE_URL = 'https://api.spotify.com/v1/'
access_token = 'BQDMPpMUGgYPkwvrQ3A7UyzMFAq3a7t0wuSqh2W1gWUxYLG-G2rs9904WHJeUCq2Iss_yee57v9iaFxgeSSOOHQObdUE4t88c822ahFUk4QpzAHFYajhsAB2kuWqZkHL3RYu4HMYTHCxItbhPhfE6IR2H9x0DM4YnsAi3Z-zIRqr9qmEX2d9e-_qdAAUhjtMLZ8w'
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}
r = requests.get(BASE_URL + 'search?q={name}&type=artist'.format(name=name), headers=headers)
r = r.json()
data={}
for i in r['artists']['items']:
    data[i['popularity']]=i['name'],i['id']
sorted(data.items(),key= lambda i:i[0],reverse=True)
print("These are the top 3 search results: ")
t=0
top={}
for i,v in data.items():
    if t<3:
     top[t+1]=[v[0],v[1]]
     print(t+1,". ",v[0])
     t+=1
    else:
        break
print("\n")
choice=int(input("Pick an artist number to get their top 3 tracks: "))
id_ = requests.get(BASE_URL + 'artists/'+top[choice][1]+'/top-tracks?market=ES',headers=headers)
id_= id_.json()
json_object = json.dumps(id_, indent = 4) 
s={}
for i in id_['tracks']:
    s[i['popularity']]=i['href'],i['name']
sorted(s.items(),key= lambda i:i[0],reverse=True)


print("These are the top 3 tracks of ",name,":")

song={}
t=0
for i,v in s.items():
    if t<3:
     top[t+1]=[v[0],v[1]]
     print(t+1,". ",v[1],':',v[0])
     t+=1
    else:
        break
print("\n")




