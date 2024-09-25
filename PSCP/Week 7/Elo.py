"""Elo"""
def elo(ra, rb, team):
    """Elo"""
    if team == "A":
        print(f"{1 / (1 + 10**((rb-ra)/400)):.02f}")
    else:
        print(f"{1 / (1 + 10**((ra-rb)/400)):.02f}")
elo(int(input()), int(input()), input())
