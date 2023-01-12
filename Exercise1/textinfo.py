def main():
    file = input("Enter name of text file: ").lower()

    with open(f'{file}') as txt_file:
        characters = len(txt_file.read())

    with open(f'{file}') as txt_file:
        upper_case = 0
        for i in txt_file.read():
            if i.isupper():
                upper_case += 1

    with open(f'{file}') as txt_file:
        lower_case = 0
        for i in txt_file.read():
            if i.islower():
                lower_case += 1

    with open(f'{file}') as txt_file:
        digits = 0
        for i in txt_file.read():
            if i.isdigit():
                digits += 1

    with open(f'{file}') as txt_file:
        white_space = 0
        for i in txt_file.read():
            if i.isspace():
                white_space += 1

    with open(f'{file}') as txt_file:
        white_space = 0
        for i in txt_file.read():
            if i.isspace():
                white_space += 1

    with open(f'{file}') as txt_file:
        a = 0
        e = 0
        i = 0
        o = 0
        u = 0
        consonant = 0
        for text in txt_file.read():
            if text.isalpha():
                if text == "a" or text == "A":
                    a += 1
                elif text == "e" or text == "E":
                    e += 1
                elif text == "i" or text == "I":
                    i += 1
                elif text == "o" or text == "O":
                    o += 1
                elif text == "u" or text == "u":
                    u += 1
                else:
                    consonant += 1

    with open(f'{file}') as txt_file:
        sentences = 0
        for text in txt_file.read():
            if text == ".":
                sentences += 1

    with open(f'{file}') as txt_file:
        line = txt_file.read().split(".")
        total = []
        for index in range(len(line)):
            count = len(line[index].split())
            if count > 0:
                total.append(count)
        average = sum(total) / len(total)

        print(f'\nStatistics for file: {file}: \n')
        print(f'Characters: {characters}')
        print(f'Upper case: {upper_case}')
        print(f'Lower case: {lower_case}')
        print(f'Digits: {digits}')
        print(f'White space: {white_space}')
        print(f"Vowels: {{'a': {a}, 'e': {e}, 'i': {i}, 'o': {o}, 'u': {u}}}")
        print(f'Consonants: {consonant}')
        print(f'Sentences: {sentences}')
        print(f"Average words per sentence: {average:.1f}")

        wait = input().lower()


if __name__ == "__main__":
    main()
