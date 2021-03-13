from collections import Counter


def read_text():
    text = ""
    pairs = []
    while True:
        text = str(input())
        if text == "0":
            break
        text = text.split(",")
        authors = text[0].split(" ")
        themes = text[1].strip().split(" ")
        for author in authors:
            for theme in themes:
                pair = (author, theme)
                pairs.append(pair)
    return pairs


def main():
    pairs = read_text()
    pairs = Counter(pairs)
    most = pairs.most_common(1)[0][1]
    pairs = dict(pairs).items()

    for element in pairs:
        if element[1] == most:
            print(element[0])


main()
