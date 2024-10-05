'''BloodDonation'''
def blood(age, w, total):
    '''sss'''
    book = "True"
    if age == 17 or 60 <= age <=70:
        book = input()
    con1 = not total and age > 55
    con2 = (age == 17 or age>=60) and book == "False"
    if 17 <= age <= 70 and w >= 45:
        if con1 or con2:
            print("No")
        else:
            print("Yes")
    else:
        print("No")
blood(int(input()),int(input()),int(input()))
