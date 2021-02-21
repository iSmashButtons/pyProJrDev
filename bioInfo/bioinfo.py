#!/usr/bin/python3
#     ____  _____ ______
#    / __ \/ ___// ____/	A Python script by Dennis Chaves
#   / / / /\__ \/ /    		github.com/ismashbuttons 
#  / /_/ /___/ / /___  		dennis@dennischaves.xyz
# /_____//____/\____/   
#                       
# bioinfo
# Ask a user for their personal information one question at a time. then check
# that the information they entered is valid. Finally, print a sunmmary of all
# the information they entered back to them.

import pyinputplus, os, subprocess

print("Who would cross the Bridge of Death must answer me these questions three ere the other side he see...")

name = pyinputplus.inputStr(prompt="What is your name? ").lower()
quest = pyinputplus.inputStr(prompt="What is your quest? ").lower()
favColor = pyinputplus.inputStr(prompt="What is your favorite color? ").lower()

if favColor.lower() == "i don't know":
    # will only work if user has firefox installed. I tried but could not find a good cross-platform solution to play the gif.
    subprocess.Popen(['firefox', "file://" + os.path.abspath('./wrong_answer.gif')])
else:
    print("So... Your name is %s. And your quest is %s. And your favorite color is %s. Alright, off you go!" %(name, quest, favColor))