"""lotto"""
def main():
    """function"""
    first = input()
    lekthai2 = input()
    lekna3_1 = input()
    lekna_2 = input()
    lekthai3_1 = input()
    lekthai3_2 = input()
    mylotto = input()
    money = 0
    nearfirst1 = ""
    nearfirst2 = ""
    if first == "000000":
        nearfirst1 = "000001"
        nearfirst2 = "999999"
    elif first == "999999":
        nearfirst1 = "999998"
        nearfirst2 = "000000"
    else:
        nearfirst1 = f"{int(first) - 1:06d}"
        nearfirst2 = f"{int(first) + 1:06d}"
    if mylotto == first:
        money += 6000000
    if mylotto in {nearfirst1, nearfirst2}:
        money += 100000
    if mylotto[-2:] == lekthai2:
        money += 2000
    if mylotto[:3] == lekna3_1:
        money += 4000
    if mylotto[:3] == lekna_2:
        money += 4000
    if mylotto[-3:] == lekthai3_1:
        money += 4000
    if mylotto[-3:] == lekthai3_2:
        money += 4000
    print(money)
main()
