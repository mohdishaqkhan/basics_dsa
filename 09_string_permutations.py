"""Generate all permutations of a string using backtracking."""

def permutations(s, index=0):
    chars = list(s)
    def backtrack(pos):
        if pos == len(chars):
            print("".join(chars))
            return
        seen = set()
        for i in range(pos, len(chars)):
            if chars[i] in seen:
                continue
            seen.add(chars[i])
            chars[pos], chars[i] = chars[i], chars[pos]
            backtrack(pos + 1)
            chars[pos], chars[i] = chars[i], chars[pos]
    backtrack(index)

if __name__ == "__main__":
    s = input("Enter a string: ")
    permutations(s)
