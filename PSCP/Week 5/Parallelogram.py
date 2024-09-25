"""Parallelogram"""
def power(txt):
    """sol"""
    count = len(txt)
    space=count-1
    decor=1
    for i in range(0,count):
        print(" "*space+txt[:decor],end="")
        decor+=1
        space-=1
        print()
    for i in range(count,1,-1):
        for j in range(i-1,0,-1):
            print(txt[count-j],end="")
        print()
power(input())
