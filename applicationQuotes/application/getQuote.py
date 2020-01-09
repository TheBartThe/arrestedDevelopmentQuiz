import random

quotes = {
    "I'm afraid I just blue myself": "Tobias",
    "I've made a huge mistake": "GOB",
    "I don't know what I expected": "Michael",
    "The seal is for marksmanship": "Buster",
    "Hey... where the f*** are my hard-boiled eggs?!": "Tobias",
    "And that's why you always leave a note": "J. Walter Weatherman",
    "OH MY GOD! THEY'RE HAVING A FIRE... sale": "Tobias",
    "Yeah, the guy in the $3,000 suit is holding the elevator for the guy who doesn’t make that in four months. Come on!": "GOB",
    "I don’t understand the question and I won’t respond to it": "Lucille",
    "She thinks I’m too critical. That’s another fault of hers": "Lucille",
    "It's hot ham water": "Lindsay",
    "I got the worst f***ing attorneys": "George Snr"
    }

def getRandomQuote():
    return random.choice(list(quotes.keys()))

#def getCorrectCharacter(quote):
#    return quotes.get(quote)

def getRandomCharacter():
    return random.choice(list(quotes.values()))

def characterChoices():
    characters = [getRandomQuote()]
    characters.append(quotes.get(quote))
    while (len(characters) < 5):
        randCharacter = getRandomCharacter()
        if (randCharacter not in characters):
            characters.add(randCharacter)
    return characters
