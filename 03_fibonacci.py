"""Find the Nth Fibonacci number (F(0)=0, F(1)=1)."""

def fibonacci(n):
    if n < 0:
        raise ValueError("N must be non-negative.")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    n = int(input("Enter N: "))
    print("Fibonacci number:", fibonacci(n))
