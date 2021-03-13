def input_month():
    month = int(input())

    return month

def make_int(str_list):
    int_list = []
    for i in str_list:
        i = int(i)
        int_list.append(i)

    return int_list

def check_for_break(some_list):
    if len(some_list) == 1:
        return True
    else:
        return False

def input_months_of_exp():
    months = []
    while True:
        month_of_exp = str(input()).split(" ")
        if check_for_break(month_of_exp):
            break
        month_of_exp = make_int(month_of_exp)
        months.append(month_of_exp[1])

    return months

def count_months(months, month):
    count = months.count(month)

    return count


month = input_month()
months = input_months_of_exp()
print(count_months(months, month))
