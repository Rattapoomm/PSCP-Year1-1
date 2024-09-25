'''align'''
def zombie(size, ans, txt):
    '''vaiable'''
    sol = size - len(txt)
    if ans == "left":
        print(txt + " " * sol)
    if ans == "center":
        left, right = (sol) // 2, (sol) // 2
        if (sol) % 2 != 0:
            left += 1
        print(" " * left + txt + " " * right)
    if ans == "right":
        print(" " * (sol) + txt)
zombie(int(input()), input().lower(), input())
