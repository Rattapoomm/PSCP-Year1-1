'''Sequence VII'''
def main():
    '''Vaiable'''
    num = int(input())
    for i in range(1,num+1):
        for j in range(1,num+1):
            if j <= i:
                print(j,end=" ")
        print()
    for F in range(1,num): 
        for k in range(num):
            if k >= F:
                print(k,end=" ")
                k -= 1
        print()
main()
