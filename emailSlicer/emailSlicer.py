#!/usr/bin/python3
#     ____  _____ ______
#    / __ \/ ___// ____/	Python script by Dennis Chaves
#   / / / /\__ \/ /    		github.com/ismashbuttons 
#  / /_/ /___/ / /___  		dennis@dennischaves.xyz
# /_____//____/\____/   
#                       
# emailSlicer
# Collect an email address from the user and then find out if the user has a
# custom domain name or a popular domain name. 

import pyinputplus, re

emailRgx = re.compile(r'([\w.-_+\*]*)(@)(\w*.com)')

popularEmailDomains = [
    'gmail.com',
    'outlook.com',
    'yahoo.com',
    'aol.com',
    'yandex.com',
    'protonmail.com',
    'zohomail.com'
]

userEmail = pyinputplus.inputEmail(prompt="Please enter your email address: ")

match = emailRgx.match(userEmail)
if match[3] in popularEmailDomains:
    print("Hi %s, your email is registered with %s. That's a really popular email provider!" %(match[1], match[3]))
else:
    print("Hi %s, your email is registered with %s. That's a unique domain!" %(match[1], match[3]))