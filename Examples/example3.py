#3 For checking prime numbers using functions
def check_prime(n):
    if n == 1 or n==0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
a=int(input("Enter a number: "))
if check_prime(a):
    print("Prime")
else :
    print("Not Prime")