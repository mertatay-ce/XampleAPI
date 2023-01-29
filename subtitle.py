from flask import Flask
import requests
from bs4 import BeautifulSoup
import json

url = "https://getyarn.io/yarn-find?text="

def jsonify(url_list,word):

    x = {

    }
    expr_list = []
    for url in url_list:
        expr = {
            'word' : word,
            'subtitle_url':url
        }
        expr_list.append(expr)
    x = expr_list
    json_file = json.dumps(x,indent=4)
    print(json_file)
    return json_file



def getting_video_urls(url):
    r = requests.get(url)
    print(r.status_code)
    soup = BeautifulSoup(r.content, "html.parser")
    cards = soup.find_all('div', {'class': 'card tight bg-w'})
    url_list = []

    for card in cards:
        url = card.a.get('href')
        #print(url[10:])
        url = url[10:]
        url_list.append(url)

    print(url_list)
    return url_list





