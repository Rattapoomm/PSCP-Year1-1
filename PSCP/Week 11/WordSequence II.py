'''Word 2'''
def pic(txt, txt_2):
    '''sol'''
    lenght = len(txt)
    lenght_2 = len(txt_2)
    indexx = 1
    indexy = 1
    if lenght <= lenght_2:
        print(txt)
        for _ in range(lenght_2):
            frist = txt_2[0:indexx]
            indexx += 1
            sec = txt[indexy:]
            indexy += 1
            #print(sec)
            print(frist+sec)
    else:
        print(txt)
        for _ in range(lenght):
            frist = txt_2[0:indexx]
            indexx += 1
            sec = txt[indexy:]
            indexy += 1
            #print(sec)
            print(frist+sec)
pic(input(), input())
