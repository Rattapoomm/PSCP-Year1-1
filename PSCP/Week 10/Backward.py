'''back'''
def step_foward():
    '''ss'''
    ans = []
    while True:
        txt_ans = input()
        if txt_ans == "NULL":
            break
        ans.append(txt_ans)
    for i in (ans[::-1]):
        print(i)
step_foward()