def get_word(values, answer=None):
    word_dict = {}
    text_file = open('temp_words.txt', 'r')
    for line in text_file.readlines():
        if line is None:
            pass
        else:
            word = line.strip().split()[0]
            word_count = word.count('') - 1
            if word_count in word_dict.keys():
                word_dict[word_count].append(word)
            else:
                word_dict[word_count] = [word]
    keys = list(word_dict.keys())
    keys.sort()
    sorted_dict = {i: word_dict[i] for i in keys}
    print(sorted_dict)
    text_file.close()
    if not answer:
        for i in range(values[0], values[-1] + 1):
            if i in sorted_dict.keys():
                print(sorted_dict[i])


def main():
    # logfile = open('log.txt', 'w')
    # logfile.close()
    # print(f"{fib(10)}, calls = {fib.count}")
    # word = input("Enter the range of word lengths (low,high):").lower()
    get_word((4, 7))


if __name__ == "__main__":
    main()
