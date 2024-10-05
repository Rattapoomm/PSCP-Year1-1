'''pong'''
def ya(num):
    '''sss'''
    ans = str(num)
    last = ans[-1:]
    if last == '3':
        print('PONG')
    elif not num %3:
        print("PONG")
    else:
        print(num)
ya(int(input()))
