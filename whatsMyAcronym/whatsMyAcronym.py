#!/usr/bin/python3
#     ____  _____ ______
#    / __ \/ ___// ____/	A Python script by Dennis Chaves
#   / / / /\__ \/ /    		github.com/ismashbuttons 
#  / /_/ /___/ / /___  		dennis@dennischaves.xyz
# /_____//____/\____/   
#                       
# whatsMyAcronym
# Ask the user to enter the full meaning of an organization or concept and
# you'll provide the acronym to the user. Examples:

import pyinputplus

print("Hello. I am a computer. I am very smart. I'm so smart, I can give you an acronym if you give me a Title!")

titleInput = pyinputplus.inputStr(prompt="What is the title of your organization or concept?\n>>> ")
wordList = titleInput.split(' ')

acronym = ''
for word in wordList:
    acronym += word[0]
print("%s is an acronym for %s!" %(acronym.upper(), titleInput.title()))