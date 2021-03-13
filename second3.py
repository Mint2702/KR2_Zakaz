import collections

def check_for_break(some_list):
    if len(some_list) == 1:
        return True
    else:
        return False

def get_authers(data):
    au = data[0].split(" ")

    return au

def get_topics(data):
    topics = data[1].strip().split(" ")

    return topics

def create_pairs(au, topics, data):
    for i in au:
        for j in topics:
            data.append((i,j))

def count_pairs(data):
    data = collections.Counter(data)
    most_common = data.most_common(1)[0][1]
    new_data = dict(data).items()
    for i in new_data:
        count = i[1]
        if count == most_common:
            print(i[0])

def input_data():
    data = []
    while True:
        info = str(input()).split(",")
        if check_for_break(info):
            break
        au = get_authers(info)
        topics = get_topics(info)
        create_pairs(au, topics, data)

    return data

data = input_data()
count_pairs(data)