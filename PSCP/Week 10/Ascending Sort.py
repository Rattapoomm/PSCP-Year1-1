'''Asc'''
def num(count):
    '''sol'''
    lst = []
    for i in range(1,count+1):
        number = int(input())
        lst.append(number)
    lst.sort()
    for i in lst:
        print(i)
num(int(input()))
