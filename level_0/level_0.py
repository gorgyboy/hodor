#!/usr/bin/python3
import requests


url = 'http://158.69.76.135/level0.php'
req = {'id': '1662', 'holdthedoor': 'submit'}

for i in range(1024):
    requests.post(url, data=req)
