"""number"""
def decoder():
    """message"""
    sentence = input()
    new_sentence = sentence.replace("13","B")
    more_new_sentence = new_sentence.replace("12","R")
    uppersentence = more_new_sentence.upper()
    decoded = ""
    for i in uppersentence:
        if i == "1":
            i = "I"
        elif i == "3":
            i = "E"
        elif i == "4":
            i ="A"
        elif i == "5":
            i = "S"
        elif i == "0":
            i = "O"
        elif i == "2":
            i = ""
        elif i == "6":
            i = ""
        elif i == "7":
            i = ""
        elif i == "8":
            i = ""
        elif i == "9":
            i = ""
        decoded += i
    print(decoded)
decoder()
