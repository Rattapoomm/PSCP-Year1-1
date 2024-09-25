'''One For All'''
def power(gen_num):
    '''Yo'''
    count = 0
    total = ""
    number = str(gen_num)
    while True:
        if count == gen_num:
            break
        count += 1
        gen_name = input()
        total += gen_name
        if count == gen_num:
            total += "_"+number
        elif not count%2:
            total += "-"*count
        elif count % 2 :
            total += "*"*count
    print(total)

power(int(input()))
