import random

correct = ["yes", "yay", "well done"]
incorrect = ["no", "unlucky", "dipshit"]

 def correct():
     return random.choice(correct)

 def incorrect():
     return random.choice(incorrect)

#def giveResult(result):
#    return random.choice(correct) if True else random.choice(incorrect)