#!/usr/bin/python3
#     ____  _____ ______
#    / __ \/ ___// ____/	A Python script by Dennis Chaves
#   / / / /\__ \/ /    		github.com/ismashbuttons 
#  / /_/ /___/ / /___  		dennis@dennischaves.xyz
# /_____//____/\____/   
#                       
# Odd or Even
# Welcome a user then ask them for a number between 1 and 1000. When the user
# gives you the number, you check if it's odd or even and then you print a
# message letting them know.

import pyinputplus


running = True
while running:
    userNumber = pyinputplus.inputInt(prompt="Enter a number between 1 and 1000\n>>> ", min=1, max=1000)
    if userNumber % 2 == 0:
        print("Congratulations! It's an even number!")
    else:
        print("Congratulations! It's an odd number!")

    reply = pyinputplus.inputYesNo(prompt="Want to have another go? ", default="no").lower()
    if reply == 'no':
        running = False
    else:
        continue
