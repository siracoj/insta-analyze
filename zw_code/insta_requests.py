#! usr/bin/env python

import requests
import os 
import glob 
import json

#pathname = '/home/wheellzarmine/Documents/pics/sun_seat.jpg'


# get file from /new folder 
picture = open(pathname)


# create request  
response = requests.get('https://api.instagram.com/v1/users/self/feed/?access_token=1569537591.32a5ddc.100e3c9ec4c048e09f0d916b53486646')


# post request 
# parse response: get status_code 
# check for post in posts 


