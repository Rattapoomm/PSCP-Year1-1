"""Squid Game 3 - Tug-of-War"""
def squid():
    """Squid Game"""
    result_team_a = 0
    result_team_b = 0
    for _ in range(10):
        team_a = int(input())
        result_team_a += team_a
    for _ in range(10):
        team_b = int(input())
        result_team_b += team_b
    if result_team_a > result_team_b:
        print("B")
    elif result_team_b > result_team_a:
        print("A")
    else:
        print("AB")
squid()
