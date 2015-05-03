#!/usr/bin/env python


# get file from /new folder 
# create request  
# post request 
# parse response: get status_code 
# check for post in posts 



"""
"""

import json
#import logging
import os
#import random
import re
#import time
from instagram import client

'''
https://api.instagram.com/v1/users/1569537591/?access_token=1569537591.32a5ddc.100e3c9ec4c048e09f0d916b53486646

https://api.instagram.com/v1/users/self/feed/?access_token=1569537591.32a5ddc.100e3c9ec4c048e09f0d916b53486646

'''


# CUSTOMISABLE
CONFIG = {
    'client_id': '32a5ddcbadd8408b9cca6937ee49df95',
    'client_secret': '48872a7263db4232a5c48ee61b1945f0',
    'redirect_uri': 'http://www.google.com',
    'access_token': '1569537591.32a5ddc.100e3c9ec4c048e09f0d916b53486646',
    'client_ips': ''
}
SEED_USER = 'wheellzarmine'
#NUM_TO_FOLLOW = 25
#NUM_TO_UNFOLLOW = 25
# END CUSTOMISABLE

# Logging stuff
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#logger = logging.getLogger(__name__)

# Global declarations
#TILES_PATH = os.getcwd()+'/Tiles.json'

api = client.InstagramAPI(**CONFIG)

def username_to_id(username):
    """Accepts a username and returns its ID."""
    user = api.user_search(q=username, count=1)
    if username != user[0].username:
        logger.error('Username to ID failed')
    #return user[0].id
    print user[0].id



#username_to_id("tomcr00k")#2210245

#username_to_id("wheellzarmine") #1569537591

#username_to_id("sadboysdonuts") #666276415

#username_to_id("myimaginarybrooklyn")