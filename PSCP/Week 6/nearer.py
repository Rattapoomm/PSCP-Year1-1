'''Nearer'''
def tim(alice,bob,car):
    '''Variable'''
    ans_1 = abs(car-alice)
    ans_2 = abs(car-bob)
    if ans_1 > ans_2:
        print(f'Bob {ans_2}')
    elif ans_1 < ans_2:
        print(f'Alice {ans_1}')
    elif ans_1 == ans_2:
        print(f'Sundaes {ans_2}')
tim(int(input()),int(input()),int(input()))
