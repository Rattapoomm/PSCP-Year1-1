"""mod doc"""
def main():
    """doc"""
    lst = input().split()
    finder = input()
    side = lst.count(finder)
    point = lst.index(finder)
    for _ in range(side):
        for _ in range(side):
            print(point, end = " ")
        print()
main()
