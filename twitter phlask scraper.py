import requests
import pprint
from requests_oauthlib import OAuth1
import json
from firebase import Firebase


config = {
    'apiKey': "AIzaSyA7xFKd3IELL5vJOGz2MapSxkuqhPDcCnE",
    'authDomain': "phlask-tweets.firebaseapp.com",
    'databaseURL': "https://phlask-tweets.firebaseio.com",
    'projectId': "phlask-tweets",
    'storageBucket': "phlask-tweets.appspot.com",
  }

firebase = Firebase(config)

auth = firebase.auth()

db = firebase.database()

data = db.get().val()

if data is None:
    data = []



query = '%23phlasktap'
url = 'https://api.twitter.com/1.1/search/tweets.json?q={}'#&count=5'
auth = OAuth1('6a0ATckFk5i2wMJmMoM2JB4WS', 'ujlN5UFsgkvAWRHl6fOSDgeYR1DoyFkdIYoMaH8CDNdSi5ktUw',
               '1114335861724844033-wJFSlUbd28ovqt8zm9b8OegOkyw0Vr', 'tIQZbJGhinI5Hf6tMcUGWdIC3R2NGEItzA1IXQJwd0Zls')



r = requests.get(url.format(query), auth=auth)
json_data = json.loads(r.content)
#pprint.pprint(r.content)


##use this for getting specific user's tweets
user_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=PHLASKecosystem'
r = requests.get(user_url, auth=auth)
json_data = json.loads(r.content)



for tweet in json_data['statuses']:
    pprint.pprint(tweet)
    
    try:
        created_at = tweet['created_at']
    except: 
        created_at = ''
    try:
        tweet_id = tweet['id']
    except: 
        tweet_id = ''
    try:
        text = tweet['text']
    except: 
        text = ''
    try:
        user = tweet['user']['name']
    except: 
        user = ''
    try:
        lat = tweet['geo']['coordinates'][0]
    except: 
        lat = ''
    try:
        long = tweet['geo']['coordinates'][1]
    except: 
        long = ''
    try:
        pic = tweet['entities']['media'][0]['media_url'] 
    except: 
        pic = ''
        
    tweet_info = {
      'created_at': created_at,
      'id': tweet_id,
      'text': text,
      'user': user,
      'lat': lat,
      'long': long,
      'picture': pic 
      }
    
    add = True
    for item in data:
        if tweet_id in item.values():
            add = False
    if add:
        data.append(tweet_info)
    
    
def save_data():
    db.child('').set(data)
    
save_data()
    
    













#tweet_info = {
#  'access': 'TrashAcademy',
#  'address': 'Linden Av NS 25ft W/O Keystone St F/W - 2',
#  'city': '',
#  'description': '',
#  'direction': 'W',
#  'filtration': '',
#  'gp_id': 'ChIJO8I7_5q0xokRPKt4aPdmmcQ',
#  'handicap': '',
#  'ill': 'Y',
#  'impressions': '43,196',
#  'lat': 40.0479,
#  'lon': -74.9969,
#  'norms_rules': '',
#  'organization': '',
#  'service': '',
#  'statement': '',
#  'tab_id': 299782,
#  'tap_type': '',
#  'tapnum': 270,
#  'unit': 97894,
#  'vessel': '',
#  'zip_code': 19114
#  }