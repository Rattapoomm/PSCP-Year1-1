"""mod doc"""
def main(txt):
    """sss"""
    lst = txt.split()
    pair = False
    for i in lst[-1::-1]:
        if not int(i)%3 or not int(i)%5:
            print(i)
            pair = True
    if not pair:
        print("Nope")
main(input())
