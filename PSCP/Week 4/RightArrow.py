"""RightArrow"""
def main():
    """RightArrow"""
    kwang = int(input())
    height = int(input())
    mid = height//2
    for i in range(height):
        if not i  or i == height-1:
            print("*"*kwang)
        elif i > height//2:
            print(" "*(mid-1)+"*"*kwang)
            mid -= 1
        else:
            print(" "*(i)+"*"*kwang)
main()