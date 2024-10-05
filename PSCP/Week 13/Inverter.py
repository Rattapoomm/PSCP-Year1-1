"""Inverter"""
def invert(s):
    """invert"""
    s = s.replace("0","I")
    s = s.replace("1","0")
    s = s.replace("I","1")
    if int(s):
        print(int(s))
invert(input())
