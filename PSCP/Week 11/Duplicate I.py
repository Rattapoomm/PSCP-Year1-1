'''Duplicate I'''
def duplicate(amount_m, amount_n, setg1, setg2):
    '''Duplicate I'''
    for _ in range(amount_m):
        group1 = input()
        setg1.add(group1)

    for _ in range(amount_n):
        group2 = input()
        setg2.add(group2)

    same = list(setg1.intersection(setg2))
    samesort = sorted(same, reverse=True)

    if len(samesort):
        for i in samesort:
            print(i)
    else:
        print("Nope")
duplicate(int(input()), int(input()), set(), set())
