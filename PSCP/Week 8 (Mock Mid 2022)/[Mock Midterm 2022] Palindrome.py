'''[Midterm 2022] Palindrome'''
def palindrome(num, time):
    '''sss'''
    count = 0
    while count != num:
        pari = "%02d" % (int(time[-2:]) + 1)
        hours = time[0:2].replace(":", "")
        if int(pari) % 60 == 0 and int(pari) != 0:
            pari = "00"
            val_y = int(hours) + 1
            hours = str(val_y)
        if int(hours) % 24 == 0:
            hours = "0"
        time = hours + ":" + pari
        if time.replace(":", "") == time.replace(":", "")[::-1]:
            count += 1
            print(time)
palindrome(int(input()), input())
