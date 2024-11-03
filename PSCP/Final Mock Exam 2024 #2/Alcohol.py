'''alcohil'''
def alcohol(sex, weight, drive, percan, al):
    """al cal"""
    can = int(input())
    hour = int(input())
    drink = ((al * percan)/100)*can
    if sex == "Male":
        mao = (drink/((weight*0.68)*10))
    elif sex == "Female":
        mao = (drink/((weight*0.55)*10))
    young_wai = mao - (0.015 * (hour))
    if drive == "Yes" and young_wai < 0.050:
        print("Safe")
    else:
        print("Not Safe")
alcohol(input(),float(input()),input(),float(input()),float(input()))
