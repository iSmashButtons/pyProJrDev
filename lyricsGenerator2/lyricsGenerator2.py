#!/usr/bin/python3
#     ____  _____ ______
#    / __ \/ ___// ____/	Python script by Dennis Chaves
#   / / / /\__ \/ /    		github.com/ismashbuttons 
#  / /_/ /___/ / /___  		dennis@dennischaves.xyz
# /_____//____/\____/   
#                       
# lyricsGenerator
# To take things a step further, have at least 3 songs by
# each artist. Ask the user to choose from a list of artists, then present
# them with a song choice.

import pyinputplus, os

def getLyricsList(artist):
    """Returns a list of available `.lyric` files in the given `artist` directory."""
    files = os.listdir(artist)
    lyricFiles = []
    for file in files:
        if file.endswith('.lyric'):
            lyricFiles.append(file)

    return lyricFiles

def getArtistDirs():
    """Returns a list of artist directories in the current directory."""
    artistDirs = []
    files = os.listdir()
    for file in files:
        if os.path.isdir(file):
            artistDirs.append(file)

    return artistDirs
            
# ask user to choose an artist
availableArtists = getArtistDirs()
artistChoice = pyinputplus.inputMenu(availableArtists, prompt="Please choose from the following artists to see the songs:\n", numbered=True)

# ask user to choose a song
songs = getLyricsList(artistChoice)
songChoice = pyinputplus.inputMenu(songs, prompt="Please select a song to see the lyrics:\n", numbered=True)

# print the contents of the lyric file
print('\n', end='')
with open(os.path.join(artistChoice, songChoice)) as fileObj:
    for line in fileObj.readlines():
        print(line, end='')
