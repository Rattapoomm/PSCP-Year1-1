"""ValidVar"""
def wrong(num):
    """sol"""
    for _ in range(num):
        text=input()
        if text in ("if" ,"else", "elif", "while","for","True","False","continue","break" ,"None", \
"return" ,"is" ,"in" ,"and" ,"or" ,"from" ,"as" ,"pass" ,"not" ,"def"):
            print("Invalid")
        elif not text.isidentifier():
            print("Invalid")
        elif text.isidentifier() or "_" in text:
            print("Valid")
wrong(int(input()))
