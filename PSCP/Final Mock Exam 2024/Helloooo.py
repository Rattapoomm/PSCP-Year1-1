'''hello'''
def four(word):
    '''sss'''
    sara = ['a','e','i','o','u']
    total = len(word)
    count = -1
    ans = ''
    final_ans = ''
    for i in word[::count]:
        if i in sara:
            final = i*4
            ans += final
            sara = []
        else:
            ans+=i
        count-=1
    for j in ans[::-1]:
        final_ans += j
    print(final_ans)                
four(input())
