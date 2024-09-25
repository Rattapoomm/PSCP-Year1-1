'''sss'''
def short():
    '''sol'''
    keep = ""
    start = None
    previous = None
    while True:
        num = int(input())
        if num == -1:
            break
        if start is None:
            start = num
            previous = num
        else:
            if previous != (num - 1):
                if start == previous:
                    keep += f"{start}, "
                else:
                    keep += f"{start}-{previous}, "
                start = num
                previous = num
            else:
                previous = num
    if start is not None:
        if start == previous:
            keep += f"{start}, "
        else:
            keep += f"{start}-{previous}, "
    print(keep.strip(", "))

short()
