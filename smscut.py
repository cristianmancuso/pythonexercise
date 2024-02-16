#SMS messages have a limitation of 160 characters. This means that you cannot send text messages that exceed 160 characters at once. If you do, the message might be truncated or split into multiple messages.Sometimes, when you write a text message, you may realize that you have exceeded the 160-character limit by just a few additional characters. This can be frustrating, especially if you don't want to edit the entire message.The task is to reduce the message to 160 characters, starting from the end of the message. To do this, you are asked to replace spaces with camelCase. This means that you should remove the spaces and change the first letter of each word that follows a space to uppercase.You continue doing this until the message is exactly 160 characters in length or less.If after making all these changes the message is still longer than 160 characters, you should simply return the resulting message without truncating or splitting it into multiple messages.

import pprint

myString = "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python web site, https://www.python.org/, and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.The Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other languages callable from C). Python is also suitable as an extension language for customizable applications.This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. It helps to have a Python interpreter handy for hands-on experience, but all examples are self-contained, so the tutorial can be read off-line as well.."


def changeString(putString):

    if len(putString) < 161: #len is lower than 161 letters
        print(myString) # print String
    elif len(putString) > 162:#if countChar is under than 162 letters
        stringTittle = myString.title() #all firts letter in each words is Upper
        convertToList = list(myString) #String  - > List
        newList = [char for char in stringTittle if char != ' '] # new list where we insert all carecters less " "
        listToString = "".join(newList) # list -> str
        howMany = len(listToString) #how many lleters we have.
        if howMany < 161: # if howmany is lower than 161
            print(listToString) #print lisToString
        else:
            pprint.pprint(myString,width=160) #print mystring with a width = 160
    else:
        raise ValueError("Error: Sorry we have an error in the code.")

        
changeString(myString)
   

