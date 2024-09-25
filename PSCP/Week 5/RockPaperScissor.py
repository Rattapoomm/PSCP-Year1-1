"""RPA"""
def beatify(text):
    """kseokfose"""
    time_arr = []
    length = len(text)
    for i in range(0,length):
        if not i % 2:
            time_arr.append(text[i:i+2])
    return time_arr
def main():
    """sfoekofkseo"""
    a_score = 0
    b_score = 0
    equal = 0
    value = beatify(input())

    for i in value:
        if i in( "RS" , "SP" , "PR"):
            a_score += 1
        elif i in ('SR', 'PS', 'RP'):
            b_score += 1
        else:
            equal += 1
    if a_score > b_score:
        print(f"A win {a_score}-{b_score}")
    elif b_score > a_score:
        print(f"B win {b_score}-{a_score}")
    else:
        print(f"DRAW {a_score}")

main()
