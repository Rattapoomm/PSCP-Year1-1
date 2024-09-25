'''diff'''
def find(n , m):
    '''sol'''
    a_set = set()
    b_set = set()
    for _ in range(n):
        txt_a = int(input())
        a_set.add(txt_a)
    for _ in range(m):
        txt_b = int(input())
        b_set.add(txt_b)
    ans = sorted(a_set-b_set)
    print(' '.join(str(item) for item in ans))
find(int(input()), int(input()))
