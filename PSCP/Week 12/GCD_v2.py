'''GCD'''
def srm(one, two):
    '''sol'''
    while two:
        one,two = two,one%two
    print(one)
srm(int(input()), int(input()))
