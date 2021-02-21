#!/usr/bin/python3
#     ____  _____ ______
#    / __ \/ ___// ____/	Python script by Dennis Chaves
#   / / / /\__ \/ /    		github.com/ismashbuttons 
#  / /_/ /___/ / /___  		dennis@dennischaves.xyz
# /_____//____/\____/   
#                       
# madLibs
# A "mad libs" generator written in python.
# A random "lib" text file is read and the user is asked to replace occurences
# of ADJECTIVE, NOUN, ADVERB, et cetera. The user words are inserted into the
# text and the finished "madlib" is output to a new text file.

import random, re
from pathlib import Path
import pyinputplus as pyip

libFile = open(f'./lib{random.randint(1,10)}.md', 'r')
story = libFile.read()

words_dict = {}
blanks = re.compile(r'`[\w\s-]+`')

wordsNeeded = blanks.findall(story)
for wordType in wordsNeeded:
    wordTypeRgx = re.compile(wordType)
    wordType = wordType.strip('`')
    reply = pyip.inputStr(f'Enter a {wordType}: ')
    story = wordTypeRgx.sub(reply,story,1)

libFile.close()
madLibFile = open(f'./madlib.md', 'w')
madLibFile.write(story)
madLibFile.close()

print(story)
