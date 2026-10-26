"""Print numbers from 1 to N using recursion."""

def print_to_n(n):
    if n < 1:
        return
    print_to_n(n - 1)
    print(n)

if __name__ == "__main__":
    n = int(input("Enter N: "))
    print_to_n(n)
