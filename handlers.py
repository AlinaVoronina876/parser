import requests
from bs4 import BeautifulSoup

def parse_iso_table(html):
    soup = BeautifulSoup(html, 'html.parser')
    klass = soup.find_all('table')[1].find_all('tr')

    currencies = []
    for row in klass:
        if row.find_all('td') == []:
            continue
        code = row.find_all('td')[0].text
        num = row.find_all('td')[1].text
        currency = row.find_all('td')[3].text
        currencies.append((code, num, currency))

    return currencies
