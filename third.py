student = str(input()).split(" ")
books = []
inp = 1
while True:
    inp = str(input())
    if inp == "0":
        break
    inp = inp.split(" ")
    if inp[0] == student[0] and inp[1] == student[1]:
        books.append(inp[2])

books.sort()
print(books[0])

    