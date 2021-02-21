#!/usr/bin/python3
#     ____  _____ ______
#    / __ \/ ___// ____/	A Python script by Dennis Chaves
#   / / / /\__ \/ /    		github.com/ismashbuttons 
#  / /_/ /___/ / /___  		dennis@dennischaves.xyz
# /_____//____/\____/   
#                       
# wordCount.py
# Ask the user what's on their mind. Then after the user responds, count the number of words in the sentence and print that as an output.

import pyinputplus

USR_STR = pyinputplus.inputStr(prompt="Hello, friend. What's on your mind?\n>>> ")
WORDS_INT = len(USR_STR.split(' '))

print("Wow. You just typed in %s words. Impressive!" %(WORDS_INT))