'''calender 2011'''
def find_day(d, m):
    '''sol'''
    if m<3:
        m+=12
        year=2010
    else:
        year=2011
    K = year%100
    J = year//100
    f=d+(13*(m+1))//5+K+(K//4)+(J//4)-(2*J)
    d_w= f%7
    days=["Saturday", "Sunday", "Monday","Tuesday", "Wednesday", "Thursday", "Friday"]\

    return days[d_w]
print(find_day(int(input()), int(input())))