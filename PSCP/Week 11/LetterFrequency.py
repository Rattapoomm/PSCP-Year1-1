'''LetterFrequency'''
def rhabet(txt):
    '''sss'''
    ans = {}
    for i in txt.lower():
        if i not in ans and i.isalpha():
            ans[i] = 1
        elif i in ans:
            ans[i] += 1
    final = max(ans, key=ans.get)
    print(final)
rhabet(input())
