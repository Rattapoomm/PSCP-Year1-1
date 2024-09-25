"""pringle"""
def pringles():
    """yum"""
    boxup = input()
    chips = input()
    boxdown = input()
    finger_length = int(input())
    if not chips[finger_length:].count(')'):
        print(chips.count(")"))
        print("None.")
        print(boxup)
        print(chips.replace(")"," "))
        print(boxdown)
    else:
        print(chips[:finger_length].count(")"))
        print("There are still some left.")
        print(boxup)
        print(chips[0:finger_length].replace(")"," ")+chips[finger_length:])
        print(boxdown)
pringles()
