"""Calculate x raised to the power n using recursion."""

def power(x, n):
    if n < 0:
        return 1 / power(x, -n)
    if n == 0:
        return 1
    half = power(x, n // 2)
    result = half * half
    return result if n % 2 == 0 else x * result

if __name__ == "__main__":
    x = float(input("Enter base x: "))
    n = int(input("Enter integer exponent n: "))
    print("Result:", power(x, n))
