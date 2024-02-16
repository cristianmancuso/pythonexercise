#Password Generator: Create a program that generates secure passwords for the user.

#primero necesitamos saber cuantos caracteres quiere la contraseña.
#segundo si quiere letras, numeros o caracteres
#tercero imprimir la contraseña.

import random

numberchar = int(input('How many characters do you want in your password? '))

letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
symbol = "!#$%&()*+,-./:;<=>?@[]^_|}~.{"
selection = [] # list where we insert symbol, number or letter.
password = [] #value where we create the password
passworddone = '' #password generate

relletter = '' #result true or false, if the user want a letter
relnumber = ''#result true or false, if the user want a number
relsymbol = ''#result true or false, if the user want a symbol

askletter = str(input("Do you want a Letters? y/n:")) #ask if the user want letters

while askletter:
    if askletter == 'y': # if write y => true
        relletter = True
        break
    elif askletter == 'n': #if write f => false
        relletter = False
        break
    elif askletter == '' or askletter == '\n':
        askletter = str(input("Do you want a Letters? y/n:")) #ask again
    else:
        askletter = str(input("Do you want a Letters? y/n:")) #ask again
        

asknumber = str(input("Do you want a Number? y/n:")) #ask if the user want numbers

while asknumber:
    if asknumber == 'y': # if write y => true
        relnumber = True
        break
    elif asknumber == 'n': #if write f => false
        relnumber = False
        break
    elif asknumber == '' or asknumber == '\n':
        asknumber = str(input("Do you want a Number? y/n:")) #ask again
    else:

        asknumber = str(input("Do you want a Number? y/n:")) #ask again
   
   
asksymbol = str(input("Do you want a Symbol? y/n:")) #ask if the user want numbers

while asksymbol:
    if asksymbol == 'y': # if write y => true
        relsymbol = True
        break
    elif asksymbol == 'n': #if write f => false
        relsymbol = False
        break
    elif asksymbol == '' or asksymbol == '\n':
        asksymbol = str(input("Do you want a Symbol? y/n:")) #ask again 
    else:
         asksymbol = str(input("Do you want a Symbol? y/n:")) #ask again
        
if relletter and relnumber and relsymbol: #add to the list letter, symbol or number.
    selection = list(letter) + list(numeros) + list(symbol)
elif relletter and relnumber:
    selection = list(letter) + list(numeros)
elif relnumber and relsymbol:
    selection = list(numeros) + list(symbol)
elif relletter and relsymbol:
    selection = list(letter) + list(symbol)
elif relletter:
    selection = list(letter)
elif relnumber:
    selection = list(numeros)
elif relsymbol:
    selection = list(relsymbol)
else:
    raise ValueError("I cant create a password because you select no in each option")

dimensionselection = int(len(selection)) #we get the len of this value

#we get the len of this value
for caracteres in range(1,numberchar+1):
    numberramdom = random.randrange(dimensionselection)
    password.append(selection[numberramdom])


passworddone = ''.join(password)
print(passworddone)