def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_up_to_n(n):
    primes = []
    for number in range(2, n + 1):
        if is_prime(number):
            primes.append(number)
    return primes

# Example usage:
n = int(input("Enter a number: "))
print("Prime numbers between 1 and", n, "are:", primes_up_to_n(n))
