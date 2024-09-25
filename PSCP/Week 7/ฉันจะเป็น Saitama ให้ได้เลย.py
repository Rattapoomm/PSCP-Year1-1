'''Saitama'''
import math
def power():
    '''Variable'''
    push = int(input())
    situp = int(input())
    upanddown = int(input())
    run = int(input())
    pushperday = int(input())
    situpperday = int(input())
    runperday = int(input())
    upanddownday = int(input())
    result_1 = math.ceil(push/pushperday)
    result_2 = math.ceil(situp/situpperday)
    result_3 = math.ceil(upanddown/upanddownday)
    result_4 = math.ceil(run/runperday)
    mix = result_1
    if result_2 >= mix:
        mix = result_2
    if result_3 >= mix:
        mix = result_3
    if result_4 >= mix:
        mix = result_4
    print(int(mix))
power()
