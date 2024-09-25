'''Bad Keyboard'''
def key(txt):
    '''sollusion'''
    ans = ""
    for i in txt:
        if i == "i":
            i = "o"
        elif i == "o":
            i = "i"
        elif i == "I":
            i = "O"
        elif i == "O":
            i = "I"
        ans += i
    print(ans)
key(input())
