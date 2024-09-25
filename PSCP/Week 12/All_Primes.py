"""pri"""
def is_prime(num):
    """nu"""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if not num % i:
            return False
    return True
def main(num1):
    """num"""
    ans = []
    for i in range(num1+1):
        if is_prime(i) is True:
            ans.append(i)
        #else:
            #print(i)
            #print("No")
    print(len(ans))
main(int(input()))
