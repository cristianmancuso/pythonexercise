# Number Guessing Game: Create a game where the computer generates a random number and the user tries to guess it.
import random

def guessnumber():
    resultado = random.randrange(100)  #we get a random number(1 at 100)
    numberuser = int(input('Insert a number: 1 at 100: ')) #user enter a number
    
    while  numberuser < 1 or numberuser > 100: #if the number is lower than 1 or is higer than 100
        print('Insert a valid number') #print a alert
        numberuser = int(input('Insert a number: 1 at 100: ')) #we ask again to insert a number
    
    while resultado != numberuser: #while the resultado and number are different
        if numberuser < resultado:
            print('The number is Higer') #Higer
        else:
            print('The number is Lower') #Lower
            
        numberuser = int(input('insert a number ')) #ask again
        
    if resultado == numberuser: #if resultado and numner are similar
        print("You won, the number is {}".format(resultado)) #print message

guessnumber()
