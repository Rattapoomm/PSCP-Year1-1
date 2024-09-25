'''Calculator'''
def math(num):
    '''sol'''
    count = ""
    for i in range(1, num+1):
        count += str(i)
    ans = len(count)
    if num == 1:
        print(1)
    else:
        print(ans+num)
math(int(input()))