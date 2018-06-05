import requests
import json
import html
import pprint
from bs4 import BeautifulSoup


response= requests.get('https://www.youtube.com/feed/trending')

bssoup = BeautifulSoup(response.text, "html.parser")

