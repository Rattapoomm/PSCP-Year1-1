'''Heron of Alexandria'''
import math
def main(a,b,c):
    '''Variable'''
    f = a+b+c
    s = f/2
    Area = math.sqrt(s*((s-a)*(s-b)*(s-c)))
    print(f'{Area:.3f}')
main(float(input()),float(input()),float(input()))
