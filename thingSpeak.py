#################ThingSpeak Test######################
############William Weiner 22Sep2018##################

import urllib.request
import time

tsAPI = 'PILI04S0O4KYN8VO'

tsURL = 'https://api.thingspeak.com/update?api_key='+tsAPI+'&field1='

urllib.request.urlopen(tsURL+"19")

