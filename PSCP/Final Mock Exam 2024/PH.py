'''Final Mock Exam'''
def color(num):
    '''sss'''
    if num>14 or num < 0:
        print('error')
    elif num == 7:
        print('neutral')
    elif num < 7:
        print('acidic')
    elif num >= 7:
        print('akaline')
color(float(input()))
