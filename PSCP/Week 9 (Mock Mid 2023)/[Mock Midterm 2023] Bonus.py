'''Bonus'''
def main(money,year,mouth):
    '''Sollusion'''
    if mouth>=10:
        year += 1
    if year>=20:
        year = 20
    ans = money*year
    if ans>=1000000:
        ans = 1000000
    if ans <=5000:
        ans = 5000
    print(ans)
main(int(input()),int(input()),int(input()))
