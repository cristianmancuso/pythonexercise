#Your friend won't stop texting his girlfriend. It's all he does. All day. Seriously. The texts are so mushy too! The whole situation just makes you feel ill. Being the wonderful friend that you are, you hatch an evil plot. While he's sleeping, you take his phone and change the autocorrect options so that every time he types "you" or "u" it gets changed to "your sister."
#Write a function called autocorrect that takes a string and replaces all instances of "you" or "u" (not case sensitive) with "your sister" (always lower case).

#Return the resulting string.

#Here's the slightly tricky part: These are text messages, so there are different forms of "you" and "u".
#For the purposes of this kata, here's what you need to support:
#"youuuuu" with any number of u characters tacked onto the end
#"u" at the beginning, middle, or end of a string, but NOT part of a word
#"you" but NOT as part of another word like youtube or bayou

import re

cadena = "You know, when you're feeling down, sometimes all u need is a little pick-me-up. And youuu  always know how to bring a smile to my face. I appreciate you so much for being there, even when I'm being a bit dramatic. Just wanted to let u know that you are awesome!"

def changeYou(txt):
    a = re.sub(r'\bYou\b', 'your sister', txt)  # Replace 'You' 
    b = re.sub(r'\bu\b', 'your sister', a)  # Replace 'u' 
    d = re.sub(r'you+u*\b', 'your sister',b) # Replace 'Youuuuuu'
    print(d)
    

changeYou(cadena)