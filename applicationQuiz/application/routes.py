from flask import redirect
from application import app
import requests
from quiz import quote, makeQuiz

@app.route('/', methods=["GET"])
def characters(quote):
    character = request.get(http://127.0.0.1:5001/<quote>)

@app.route('/<boolean:correct>', methods=["GET"])
def result(correct):
    return getResult(correct)