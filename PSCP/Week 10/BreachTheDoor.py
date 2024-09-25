'''BreachTheDoor'''
import re
def six(txt):
    '''sss'''
    final_ans = []
    txt_new = re.sub(r'[! @ # $ % ^ & * ( ) _ + - = : ; < > , . / \ | ? ~ © ® ™ §]',' ', txt)
    ans = txt_new.split()
    for i in ans:
        final = len(i)
        if i.isalpha():
            if final > 6:
                final_ans.append(i)
    print(*final_ans)
six(input())