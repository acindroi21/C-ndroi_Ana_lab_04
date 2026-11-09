
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def goldbach(n):
    for p in range(2, n // 2 + 1):
        q = n - p

        if is_prime(p) and is_prime(q):
            print(p, "+", q, "=", n)

def main():
    try:
        n = int(input("Enter an even natural number greater than 2: "))
        if n <= 2 or n % 2 != 0:
            print("The number must be even and greater than 2.")
        else:
            print("Goldbach decompositions:")
            goldbach(n)
    except ValueError:
        print("Please enter a natural number.")

main()
