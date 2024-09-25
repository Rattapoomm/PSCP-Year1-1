'''Milk'''
def milk(a,b,c,d):
    '''Variable'''
    cap = 0
    ans = 0
    result = 0
    if not b:
        result = d//a
    elif b > c:
        ans = d//a
        result += ans
        cap += ans
    while cap >= b > 0:
        cap -= b
        result += c
        cap += c
    print(result)
milk(int(input()),int(input()),int(input()),int(input()))
