'''remove'''
import re
def ahr(txt):
    '''sss'''
    ans = re.sub(r'<.*?>'," ", txt)
    final = ans.split()
    print(final)
ahr(input())
