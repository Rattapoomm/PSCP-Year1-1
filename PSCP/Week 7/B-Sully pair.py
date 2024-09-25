"""fully pair"""
def main():
    """main"""
    counter = ""
    result = ""
    text = input()
    for i in text:
        if counter.count(i) < 1:
            counter += i
    for j in counter:
        if text.count(j) %2:
            result += j
    if not result:
        print("fully paired")
    else:
        print(result)
main()
