'''[Final 2021] Music Lover'''
import re
def musicc(num):
    '''sss'''
    for _ in range(num):
        txt = input()
        result = re.sub(r'-',' ',txt)
        print(result)
musicc(int(input()))