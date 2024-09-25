'''Seq'''
def pic(txt):
    '''sol'''
    lenght = len(txt)
    indexx = 1
    for _ in range(lenght):
        print(txt[0:indexx])
        indexx += 1
pic(input())
