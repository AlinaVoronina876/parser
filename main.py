from handlers import parse_iso_table

url = 'https://en.wikipedia.org/wiki/ISO_4217'

def main():
    print('Code  ', 'Num   ', 'Currency   ')
    currencies = parse_iso_table(text)

    for code, num, currency in currencies:
        print(f'{code}   {num}   {currency}')

if __name__ == "__main__":
    main()