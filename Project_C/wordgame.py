import collections
import random
import sys


def get_word():
    word_dict = {}
    text_file = open('words.txt', 'r')
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
    text_file.close()
    return sorted_dict


def select_word(words, w_range, answer=None):
    cut_list = {}
    for i in range(w_range[0], w_range[-1] + 1):
        if i in words.keys():
            cut_list[i] = words[i]
    if not answer:
        return random.choice(words[w_range[-1]]), cut_list
    else:
        return answer, cut_list


def generate_list(w):
    player_dict = {}
    for i in w[-1].keys():
        perm_list = []
        for v in w[-1][i]:
            if collections.Counter(w[0]) >= collections.Counter(v):
                perm_list.append(v)
                perm_list.sort()
        if perm_list:
            player_dict[i] = perm_list
    return w[0], player_dict


def game(start):
    word = start[0]
    w_dict = start[-1]
    game_list = []
    for length in w_dict.keys():
        blank_list = []
        for w in w_dict[length]:
            blank_list.append(str(w).replace(w, "-" * length))
        if blank_list:
            game_list.append(blank_list)

    player_answer = ""
    while player_answer != "q":
        word = list(word)
        random.shuffle(word)
        word = ''.join(word)
        print(word)
        for i in game_list:
            print(i)

        player_answer = input("Enter a guess:").lower()
        if len(player_answer) in w_dict.keys():
            for i in w_dict[len(player_answer)]:
                is_correct = False
                if player_answer == i:
                    is_correct = True
                    break
        else:
            is_correct = False

        if is_correct:
            print("correct")
            # I need to find the index the word is at and replace that index instead of remaking the list every time
            keys = list(w_dict.keys())
            word_pos = 0
            found = False
            for length in w_dict.keys():
                word_pos = 0
                for w in w_dict[length]:
                    if w == player_answer:
                        found = True
                        break
                    word_pos += 1
                if found:
                    break
            list_index = keys.index(length)
            game_list[list_index][word_pos] = player_answer
        elif player_answer == "q":
            end_list = []
            for i in w_dict.values():
                for v in i:
                    end_list.append(v)
            print(end_list)
        else:
            print("Sorry. Try again")


def main():
    # logfile = open('log.txt', 'w')
    # logfile.close()
    # print(f"{fib(10)}, calls = {fib.count}")
    # word = input("Enter the range of word lengths (low,high):").lower()
    word_range = (4, 6)
    word_list = get_word()
    # figure out how to launch with system
    word = select_word(word_list, word_range, answer=None)
    game_ready = generate_list(word)
    game(game_ready)


if __name__ == "__main__":
    main()
