'''line sorting'''
def sort_lines():
    '''dispep 8 '''
    num = int(input())
    my_list = []
    for _ in range(num):
        txt = input()
        my_list.append(txt)

    sorted_list = sorted(my_list, key=len)
    for line in sorted_list:
        print(line)

if __name__ == "__main__":
    sort_lines()
