'''Median'''
def cal(count):
    '''sol'''
    lit = []
    ans = 0
    sol = 0
    for _ in range(count):
        txt = float(input())
        lit.append(txt)
    lit.sort()
    n_var = len(lit)
    #total = (lit[n_var] + 1)/2
    #if not len(lit) % 2:
        #total = (lit[n_var] + lit[n_var+1] + 1)/2
    if n_var %2:
        ans = n_var//2
        print(f'{lit[ans]:.3f}')
    elif not n_var %2:
        ans = n_var//2
        sol = (lit[ans-1]+lit[ans])/2
        print(f'{sol:.3f}')
cal(int(input()))
