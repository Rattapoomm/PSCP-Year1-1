'''sss'''
def Road(txt):
    '''sol'''
    if txt < 0:
        print('InValid')
    elif txt <= 5.032:
        print('Bangkok')
    elif 5.032 < txt <= 35.477:
        print('Samut Prakarn')
    elif 35.477 < txt <= 52.900:
        print('Chachoengsao')
    elif 52.900 < txt <= 58.855: 
        print('Chon Buri')
    else:
        print('InValid')

Road(float(input()))
