from quotes_library import get_quotes

def main():
    print("HELLO QUOTE LOVER!")
    while True:
        key = input("Hit any key to get a quote or enter q to quit:  ").lower()

        if key == "q":
            print("Good Bye!")
            break


        quote = get_quotes(random=True)
        print(quote)
        lsdata = quote['data']
        for i in lsdata:
            dicto = i

            key = "quote"

            print(dicto[key])

main()