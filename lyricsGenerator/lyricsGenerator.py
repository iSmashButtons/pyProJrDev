#!/usr/bin/python3
#     ____  _____ ______
#    / __ \/ ___// ____/	Python script by Dennis Chaves
#   / / / /\__ \/ /    		github.com/ismashbuttons 
#  / /_/ /___/ / /___  		dennis@dennischaves.xyz
# /_____//____/\____/   
#                       
# lyricsGenerator
# Ask a user to choose from a list of 10 songs. Print out the lyrics to the
# song they selected. 

import pyinputplus, os

# create a list of the lyrics available
files = os.listdir()
lyricFiles = []
for file in files:
    if file.endswith('.lyric'):
        lyricFiles.append(file)

# ask user to choose a song
response = pyinputplus.inputMenu(lyricFiles, prompt="Please choose from the following songs to see the lyrics:\n", numbered=True)

# print the contents of the lyric file
print('\n', end='')
with open(response) as fileObj:
    for line in fileObj.readlines():
        print(line, end='')
