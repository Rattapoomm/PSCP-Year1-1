"""Filter"""
import json
def jsonnnnnnnnnnnn():
    """Function"""
    scap = json.loads(input())
    socre = float(input())
    ans = []
    for i in scap:
        if scap[i] >= socre:
            ans.append(i)
    if not ans:
        print("Nope")
    else:
        for i in sorted(ans):
            print(f"{i}\t{scap[i]:.2f}")
jsonnnnnnnnnnnn()