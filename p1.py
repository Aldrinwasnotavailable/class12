def check_if_prime(num):
    # Check if a number is a prime number
    if num <= 1:
        return False
    for i in range(2, int(num)+1):
        if num % i == 0 and num!= i:
            return False
    return True

num = int(input("Enter a number: "))

if check_if_prime(num):
    print(f"{num} is a prime number.")