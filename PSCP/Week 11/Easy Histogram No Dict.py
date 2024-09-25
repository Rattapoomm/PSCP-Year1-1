'''easy histogam'''
def count_chars():

    """function"""
    text = input()
    chars = []
    counts = []

    for char in text:
        if char.isalpha():
            if char in chars:
                index = chars.index(char)
                counts[index] += 1
            else:
                chars.append(char)
                counts.append(1)

    def sort_key(pair):
        """FUNCTION"""
        char, _ = pair
        return char.lower(), char.isupper(), char

    sorted_chars = sorted(zip(chars, counts), key=sort_key)

    for index, (char, count) in enumerate(sorted_chars):
        print(char + ' = ' + str(count))

count_chars()
