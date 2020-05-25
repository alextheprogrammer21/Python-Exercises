#!/usr/bin/env python

import requests

def download(url): 
    get_response = requests.get(url)
    print(get_response.content)

download("https://www.tibco.com/blog/wp-content/uploads/2020/01/TIBCOandPython-1-scaled-e1579201642399.jpg")