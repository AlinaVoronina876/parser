from handlers import get_request

url = 'https://en.wikipedia.org/wiki/ISO_4217'

def main():
    print('Code  ', 'Num   ', 'Currency   ')
    text = get_request(url)

if __name__ == "__main__":
    main()