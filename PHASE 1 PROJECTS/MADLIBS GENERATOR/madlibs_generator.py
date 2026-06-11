def main():

    with open('madlib.txt', 'r', encoding='utf-8')as file:
        data = file.read()
        start = -1
        slices = set()

        placeholder_start, placeholder_end = 0,0

        START_SLICE = "<"
        END_SLICE = ">"

        for idx, char in enumerate(data):
            if char == START_SLICE:
                placeholder_start = idx

            if char == END_SLICE:
                placeholder_end = idx + 1

                placeholder = data[placeholder_start:placeholder_end]

                slices.add(placeholder)


    for placeholder in slices:
        replace = input(f"Enter a {placeholder}: ")
        data = data.replace(placeholder, replace)

    print(data)


if __name__ == "__main__":
    main()