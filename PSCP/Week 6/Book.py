'''Books'''
import math
def books(amount, pages, x, y):
    '''sol'''
    page = 0
    day = 0
    count = 0
    while True:
        processpage = math.ceil((x / y) * pages)
        if amount == count:
            break
        if processpage >= pages:
            break
        page += processpage
        if page >= pages:
            count += 1
            page = 0
        x += 1
        y += 1
        day += 1
    day += amount - count
    print(day)
books(int(input()), int(input()), int(input()), int(input()))
