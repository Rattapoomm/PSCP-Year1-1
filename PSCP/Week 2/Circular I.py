"""Burhhh"""
x = float(input())
y = float(input())
radius = float(input())
x2 = float(input())
y2 = float(input())
if ((x - x2)**2 + (y - y2)**2)**0.5 <= radius:
    print("Yes")
else:
    print("No")
