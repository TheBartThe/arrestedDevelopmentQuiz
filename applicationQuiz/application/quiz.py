import requests

def makeQuiz(quoteService):
    choices = request.get(quoteService)
    quote = choices.pop(0)
    answer = choices[0]
    random.shuffle(choices)
    quiz = [quote, answer, choices]
    return quiz

def checkAnswer():
    test

def getResult(correct):
    return request.get(resultService)