'''home run'''
def best(time,side):
    '''sol'''
    count = 0
    ans =  0
    while True:
        if count == time:
            break
        stret = float(input())
        count += 1
        if side > stret:
            ans += 1
    print(ans)
best(int(input()),float(input()))
