"""Print all subsequences of a string using recursion."""

def subsequences(s, index=0, current=""):
    if index == len(s):
        print(repr(current))
        return
    subsequences(s, index + 1, current)
    subsequences(s, index + 1, current + s[index])

if __name__ == "__main__":
    s = input("Enter a string: ")
    subsequences(s)
