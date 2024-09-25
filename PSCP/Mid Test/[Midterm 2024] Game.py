"""Game"""
def game(a,b):
    """Game"""
    if a%3 == b%3:
        print(a%3)
    else:
        print("Error")
game(int(input()),int(input()))
