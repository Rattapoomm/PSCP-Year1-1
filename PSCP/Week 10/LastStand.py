"""mod doc"""
import json
def main():
    """doc"""
    lst = json.loads(input())
    for i in lst:
        print(str(i)[-1])
main()
