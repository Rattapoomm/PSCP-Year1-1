'''Cha Cha Cha'''
import math
def work(day):
    '''Variable'''
    count = 0
    total = 0
    while True:
        if day == count:
            break
        time_work = float(input())
        result = math.ceil(time_work)
        ans = result*8720
        total += ans
        count += 1
    print(int(total))
work(int(input()))
