from collections import Counter


def main():
    with open("Strings.txt") as IN_FILE:
        data = ""
        for i in IN_FILE.read().lower():
            if i.isalpha() or i == "'" or i.isspace():
                data += i
            else:
                data += " "

    data = data.strip().split()
    d = Counter(data)
    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

    length = 0
    for keys in d:
        if len(keys) > length:
            length = len(keys)

    with open("wc.txt", "w") as OUT_FILE:
        for keys in d:
            value = keys + ":"
            OUT_FILE.write(f"{value:>{length + 1}} {d[keys]}\n")


if __name__ == "__main__":
    main()
