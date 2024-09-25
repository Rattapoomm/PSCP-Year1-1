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
    if is_prime(num1) is True:
        print("Yes")
    else:
        print("No")
main(int(input()))