"""ball"""
def main(height):
    """sss"""
    count = -1
    while height >= 0.01:
        height = height * 3 / 5
        count += 1
    print(count)
main(float(input()))
