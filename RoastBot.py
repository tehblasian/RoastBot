from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from random import randint

app = Flask(__name__)

InsultList = ["You're a LOSER", 'Suck it', 'OP is a phaggot', 'come at me, bro', 'Please stop talking to me']


@app.route("/", methods=['GET', 'POST'])
def run():
    reply = selectreply()
    roast(reply)


def roast(reply):
    """Respond to incoming texts"""
    response = MessagingResponse().message(reply)
    return str(response)


def selectreply():
    random = randint(0, len(InsultList))
    return InsultList[random]
