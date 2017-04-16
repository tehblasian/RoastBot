from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from bs4 import BeautifulSoup
from random import randint
import requests

app = Flask(__name__)

InsultList = ["You're a LOSER", 'Suck it', 'OP is a phaggot', 'come at me, bro', 'Please stop talking to me']


@app.route("/", methods=['GET', 'POST'])
def run():
    """Respond to incoming texts"""
    if randint(0, 1) == 0:
        insult = InsultList[randint(0, len(InsultList))]
    else:
        insult = getRandomInsult()
    response = MessagingResponse().message(insult)
    return str(response)


def getRandomInsult():
    page = requests.get('http://www.randominsults.net/')
    soup = BeautifulSoup(page.content, 'html.parser')
    insult = soup.find_all('i')[0].get_text()
    return insult
