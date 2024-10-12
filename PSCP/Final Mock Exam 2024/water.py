'''water'''
def cal():
    n = int(input())
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    total = 0
    ans = 0
    for _ in range(n):
        txt = float(input())
        if txt<=b:
            total = txt*a
            if total<=d:
                total = 0
        elif txt>=b:
            more = txt-b
            total=((b*a)+(more*c))
            if total<=d:
                total= 0
        ans+=total
    print(f'{ans:.2f}')
cal()
