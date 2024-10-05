"""Matrix_MN"""
def mat(m,n):
    """matrix"""
    lst = []
    lst_1 = []
    for _ in range(m):
        for _ in range(n):
            lst_1.append(input())
        lst.append(lst_1)
        lst_1 = []
    for k in range(m):
        for l in range(n):
            print(lst[k][l],end=" ")
        print()

mat(int(input()),int(input()))
