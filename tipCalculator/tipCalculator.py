#!/usr/bin/python3
#     ____  _____ ______
#    / __ \/ ___// ____/	Python script by Dennis Chaves
#   / / / /\__ \/ /    		github.com/ismashbuttons 
#  / /_/ /___/ / /___  		dennis@dennischaves.xyz
# /_____//____/\____/   
#                       
# tipCalculator
# Your goal is to find out exactly how much tip you should give after receiving
# a service. In this scenario, ask for the total bill. Then display the tip for
# 18%, 20%, and 25%.

import pyinputplus

bill = pyinputplus.inputFloat(prompt="Enter the total bill amount: ")
tip = {
    18: bill * 0.18,
    20: bill * 0.20,
    25: bill * 0.25
}

print(' ' * 5, 'tip'.ljust(8), 'total'.rjust(8))
for key in tip.keys():
    print(str(key) + '%: ', "$%.2f".ljust(8) %(tip[key]), "$%.2f".rjust(8) %(tip[key] + bill))