"""Find the factorial of N using recursion."""

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    n = int(input("Enter N: "))
    print("Factorial:", factorial(n))
