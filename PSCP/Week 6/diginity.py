"""Diginity"""
def result(number):
    """help Function"""
    now_number = 0
    for i in number:
        now_number += int(i)
    return now_number
def main():
    """main"""
    number = int(input())
    while number:
        while number >= 10:
            number = result(str(number))
        print(number)
        number = int(input())
main()
