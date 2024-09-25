"""Bubble"""
def solid(txt) :
    """Sol"""
    cnt = 0
    n = 0
    while n < len(txt) - 1 :
        c = 0
        if txt[n] == "^" :
            cnt += 1
            n += 1
        elif txt[n].islower() :
            cnt += 1
            n += 1
        elif txt[n].isupper() :
            cnt += 1
            n += 3
            if n >= len(txt) - 1 :
                break
            if txt[n].islower() :
                n -= 1
                c += 1
            if txt[n].islower() :
                n -= 1
                c += 1
            if not txt[n].isupper() :
                n += c
            if txt[n].isspace() :
                n -= 1
            if txt[n].isspace() :
                n -= 1
        if txt[n].isspace() :
            print("IMPOSSIBLE")
            print(len(txt) - n)
            return
    print("POSSIBLE")
    print(cnt)
solid(input())
