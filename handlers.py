import requests
from bs4 import BeautifulSoup

def get_request(url):
    responses = requests.get(url)
    return responses.text

