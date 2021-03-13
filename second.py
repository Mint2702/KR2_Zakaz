from collections import Counter

inp = 1
pairs = []
while True:
    inp = str(input())
    if inp == "0":
        break
    inp = inp.split(",")
    authers = inp[0].split(" ")
    themes = inp[1].strip().split(" ")
    for auther in authers:
        for theme in themes:
            pair = (auther, theme)
            pairs.append(pair)

pairs = Counter(pairs)
most = pairs.most_common(1)[0][1]
pairs = dict(pairs).items()
for element in pairs:
    if element[1] == most:
        print(element[0])
