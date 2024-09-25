'''Turnstile'''
def lock():
    '''Variable'''
    count = 0
    result = ""
    action = input()
    while action != "END":
        result += action
        if "CP" in result:
            count += 1
            result = ""
        action = input()
    print(count)
lock()
