month = str(input())

inp = 1
count = 0
while True:
    inp = str(input())
    if inp == "0":
        break
    inp = inp.split(" ")
    if inp[1] == month:
        count += 1

print(count)