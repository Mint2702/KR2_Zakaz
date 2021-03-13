def find_books():
    books = []
    student = str(input())
    student = student.split(" ")
    while True:
        text = str(input())
        if text:
            if text == "0":
                break
            text = text.split(" ")
            if text[0] == student[0] and text[1] == student[1]:
                books.append(text[2])
        else:
            break
    return books


def main():
    books = find_books()
    books.sort()
    print(books[0])


main()
