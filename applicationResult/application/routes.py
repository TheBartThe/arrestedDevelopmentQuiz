from flask import redirect
from application import app
import requests
from result import giveResult

@app.route('/correct', methods=["GET"])
def correctAnswer():
    return correct()

@app.route('/incorrect', methods=["GET"])
def incorrectAnswer():
    return incorrect()