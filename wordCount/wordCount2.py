#!/usr/bin/python3
#     ____  _____ ______
#    / __ \/ ___// ____/	A Python script by Dennis Chaves
#   / / / /\__ \/ /    		github.com/ismashbuttons 
#  / /_/ /___/ / /___  		dennis@dennischaves.xyz
# /_____//____/\____/   
#                       
# wordCount.py
# Open a text file that is passed in as argument, count the number of words in
# there and print out the sum total.

import sys

fileObj = open(sys.argv[1], 'r')
text = fileObj.read()
fileObj.close()
words = text.split(' ')
print("There are %s words in that file." %(len(words)))