"""Run Length Encoding"""
def sad():
    """sol"""
    word=input()
    count=1
    bad=""
    for i in range(1,len(word)):
        if word[i]==word[i-1]:
            count+=1
        else:
            bad+=str(count)+word[i-1]
            count=1
    bad+=str(count)+word[-1]
    print(bad)
sad()
