needed_month = str(input())

counter = 0
data = [needed_month, 1]
while len(data) > 1:
    data = str(input()).split(" ")
    if len(data) > 1:
        moth_of_exp = 1
        if data[1] == needed_month:
            counter = counter + 1

print(counter)