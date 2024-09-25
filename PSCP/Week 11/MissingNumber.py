'''miss'''
def lost(num):
    '''sol'''
    my_dict = {i: i for i in range(1,num+1)}
    while True:
        txt = int(input())
        if not txt:
            break
        if txt in my_dict:
            del my_dict[txt]
    for i in my_dict:
        print(i)
lost(int(input()))
