#!/usr/bin/python3
#     ____  _____ ______
#    / __ \/ ___// ____/	A Python script by Dennis Chaves
#   / / / /\__ \/ /    		github.com/ismashbuttons 
#  / /_/ /___/ / /___  		dennis@dennischaves.xyz
# /_____//____/\____/   
#                       
# rockPaperScissors
# Play a game of rock paper scissors against the computer

import random, pyinputplus, time

def printOutcome(winner):
    global userWeapon, compWeapon
    """Print a message describing the output of the match."""
    if winner == None:
        print("\nHuzzah! It's a draw!\n")
        time.sleep(2)
    else:
        print("\nHuzzah! You threw %s, I threw %s! %s wins!\n" %(userWeapon, compWeapon, winner.title()))
        time.sleep(2)

def matchOutcome(matchTuple):
    """Determine the outcome of the match based on the input tuple of two weapons."""
    global userWins, compWins
    winner = None

    # user throws rock
    if matchTuple == ('rock', 'paper'):
        winner = 'computer'
        compWins += 1
    elif matchTuple == ('rock', 'scissors'):
        winner = 'user'
        userWins += 1

    # user throws paper
    elif matchTuple == ('paper', 'rock'):
        winner = 'user'
        userWins += 1
    elif matchTuple == ('paper', 'scissors'):
        winner = 'computer'
        compWins += 1

    # user throws scissors
    elif matchTuple == ('scissors', 'rock'):
        winner = 'computer'
        compWins += 1
    elif matchTuple == ('scissors', 'paper'):
        winner = 'user'
        userWins += 1

    return winner

print("Who dares to challenge the computer in a competition of rock, paper, and scissor?")

weapons = ['rock', 'paper', 'scissors']
userWins = 0
compWins = 0

while (userWins < 2) and (compWins < 2):
    print("\nBring forth your fist! Or press enter to flee like the coward you are!")
    compWeapon = weapons[random.randint(0,2)]
    userWeapon = pyinputplus.inputChoice(['rock', 'paper', 'scissors'], blank=True)
    match = (userWeapon, compWeapon)
    if userWeapon == '':
        break
    else:
        printOutcome(matchOutcome(match))

if userWins > compWins:
    print("Gah! You have defeated me!")
else:
    print("Bwahaha! You loose!")