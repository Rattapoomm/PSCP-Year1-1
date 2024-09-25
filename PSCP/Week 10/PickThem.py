'''PickThem'''
import json
def double(txt):
    '''sol'''
    lst = json.loads(txt)
    pair = False
    for i in lst:
        if not i%2:
            print(i)
            pair = True
    if not pair:
        print("Nope")
double(input())
