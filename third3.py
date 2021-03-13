

def take_student():
    student = str(input())
    student = student.split(" ")
    return student


def take_books(student):
    books = []
    text = ""
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


def find_book():
    student = take_student()
    books = take_books(student)
    books.sort()
    book = books[0]
    return book


result = find_book()
print(result)
