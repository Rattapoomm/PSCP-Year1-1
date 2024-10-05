"""CoinChangev1"""
def coin(c):
    """C"""
    twentyfive,remains = divmod(c,25)
    ten , remains = divmod(remains,10)
    five , one = divmod(remains,5)
    print(twentyfive+ten+five+one)
coin(int(input()))
