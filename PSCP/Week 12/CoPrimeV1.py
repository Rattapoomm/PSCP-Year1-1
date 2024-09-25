'''CoPrimeV1'''
def srm(one, two):
    '''sol'''
    while two:
        one,two = two,one%two
    if one == 1:
        print("YES")
        print(1)
    else:
        print("NO")
        print(one)
srm(int(input()), int(input()))