'''Longer'''
import math
def long(r,a,b):
    '''sollusion'''
    Circle = 2*math.pi*r
    square = a+a+b+b
    if Circle>square:
        print("Circle is longer")
        ans = Circle-square
        print(f'{ans:.5f}')
    elif Circle < square:
        print("Rectangle is longer")
        ans = square-Circle
        print(f'{ans:.5f}')
    elif Circle == square:
        print("Equal")
        ans = Circle-square
        print(f'{ans:.5f}')
long(float(input()),float(input()),float(input()))
