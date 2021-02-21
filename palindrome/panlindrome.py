#!/usr/bin/python3
#     ____  _____ ______
#    / __ \/ ___// ____/	Python script by Dennis Chaves
#   / / / /\__ \/ /    		github.com/ismashbuttons 
#  / /_/ /___/ / /___  		dennis@dennischaves.xyz
# /_____//____/\____/   
#                       
# panlindrome
# Ask the user for five input words. Then check if any of those words are
# palindromes. A palindrome is a word or phrase that remains the same whether
# it's read forward or backward. This script only checks for words that are
# palindromes, not phrases. Example palindrome words:
# - racecar
# - solos
# - kayak

import pyinputplus

def reverseWord(w):
    """Takes an input word `w`, reverses the spelling, and returns the result."""
    reversedWord = ''
    for i in range(1, len(w) + 1):
        reversedWord += w[0-i]

    return reversedWord

print("Give me five words and I will tell you if any of them is a palindrome.\n")

# Get words from user
words = []
while len(words) < 5:
    reply = pyinputplus.inputStr(prompt="Enter a word (%s/5): " %(len(words)+1))
    if len(reply.split(' ')) > 1:
        print("One word at a time please.")
        continue
    else:
        words.append(reply)

# check for palindromes
for word in words:
    # reverse the letters in the word
    reversedWord = reverseWord(word)
    if word == reversedWord:
        print("%s is a palindrome!" %(word))
    else:
        continue