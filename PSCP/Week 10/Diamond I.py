'''Dai'''
def plus(num, per_senten):
    '''sss'''
    count = 0
    total = 3
    loca = 0
    ans = []
    for _ in range(num):
        txt = input()
        new = txt.split()
        ans.extend(new)
    #for _ in range(num):
    #print(ans[9])
    #print(ans[19])
    #print(ans[29])
    #while count == total:
    print(int(ans[loca]))+(int(ans[int(loca)+int(per_senten)]))


plus(int(input()), int(input()))