"""kaprekar"""
def kaprekarcal(num, prev, counter):
    """function"""
    if not num :
        return counter

    prev = num

    digits = [0] * 4
    for i in range(4):
        digits[i] = num % 10
        num = num // 10

    for i in range(4):
        for j in range(i + 1, 4):
            if digits[i] > digits[j]:
                digits[i], digits[j] = digits[j], digits[i]

    asc = 0
    for i in range(4):
        asc = asc * 10 + digits[i]

    for i in range(4):
        for j in range(i + 1, 4):
            if digits[i] < digits[j]:
                digits[i], digits[j] = digits[j], digits[i]

    desc = 0
    for i in range(4):
        desc = desc * 10 + digits[i]

    diff = abs(asc - desc)

    if diff == prev:
        return counter

    counter += 1
    return kaprekarcal(diff, prev, counter)

def kaprekar(num):
    """function"""
    return kaprekarcal(num, 0, 0)

def main():
    """function"""
    num = int(input())
    if 1000 <= num <= 9999:
        counter = kaprekar(num)
        print(counter)

main()
