'''color'''
def mix(one, two):
    '''sss'''
    ans = []
    right = {'Red','Yellow','Blue'}
    if one in right:
        ans.append(one)
        if two in right:
            ans.append(two)
            if one == two:
                print(one)
            elif 'Red' in ans:
                if 'Yellow' in ans:
                    print('Orange')
                elif 'Blue' in ans:
                    print('Violet')
            elif 'Yellow'in ans:
                if 'Blue' in ans:
                    print('Green')
            else:
                print('Error')
        else:
            print('Error')
    else:
        print('Error')
mix(input(), input())
