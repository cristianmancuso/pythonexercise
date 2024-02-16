#Text Analysis Exercise
#1. Ask the user to input a sentence.
#2. Split the sentence into words.
#3. Count the number of words in the sentence.
#4. Find the longest word in the sentence.
#5. Replace all vowels in the sentence with the letter 'x'.
#6. Convert all letters in the sentence to uppercase.
#7. Print the results.

sentence = 'Hello, I want to dance, supercalifragilisticexpialidocious'

def splitSentence(text):
    print(text.split())

def countWords(text):
    splitWords = text.split()
    print(len(splitWords))

def findLongestWord(text):
    longestWord = (min(text.split(), key=len))
    print(longestWord)

sentence2 = 'hello yes, I want to dance yes, I want to dance'

def replaceVowelsWithX(text):
    print(textToList)
    for i in range(len(textToList)):
        if textToList[i] in 'aeiouAEIOU': # If the character is a vowel
            textToList[i] = 'X' # Replace the vowel with 'X'
    modifiedText = ''.join(textToList) # Convert the list of characters back to a string
    print(modifiedText) # Print the modified string

def allToUppercase(text):
    uppercaseText = text.upper()
    print(uppercaseText)

def printResult():
    splitSentence(sentence)
    countWords(sentence)
    findLongestWord(sentence)
    replaceVowelsWithX(sentence2)
    allToUppercase(sentence2)

printResult()         