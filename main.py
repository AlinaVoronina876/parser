from handlers import get_request, parse_iso_table

url = 'https://en.wikipedia.org/wiki/ISO_4217'

def main():
    print('Code  ', 'Num   ', 'Currency   ')
    text = get_request(url)
    currencies = parse_iso_table(text)

    for code, num, currency in currencies:
        print(f'{code}   {num}   {currency}')

if __name__ == "__main__":
    main()