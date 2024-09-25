'''Divide'''
def three_five(num):
    '''sol'''
    ans = []
    for i in range(num+1):
        if  not i % 3 or not i % 5:
            ans.append(i)
    print(sum(ans))
three_five(int(input()))
