from flask import redirect
from application import app
import requests
from getQuote import getRandomQuote, characterChoices

@app.route('/', methods=["GET"])
def characters(quote):
    return characterChoices()

#@app.route('/character/<string:quote>', methods=["GET"])
#def characters(quote):
#    return getCorrectCharacter(quote)