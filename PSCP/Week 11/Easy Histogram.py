'''easy histogam'''
def sss():

    """function"""
    text = input()
    chars = []
    total = []

    for char in text:
        if char.isalpha():
            if char in chars:
                index = chars.index(char)
                total[index] += 1
            else:
                chars.append(char)
                total.append(1)

    def sort_key(pair):
        """FUNCTION"""
        char, _ = pair
        return char.lower(), char.isupper(), char

    sorted_chars = sorted(zip(chars, total), key=sort_key)

    for index, (char, total) in enumerate(sorted_chars):
        print(char + ' = ' + str(total))

sss()
