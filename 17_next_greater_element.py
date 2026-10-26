"""Find the next greater element to the right for each list item."""

def next_greater(arr):
    result = [-1] * len(arr)
    stack = []
    for i, value in enumerate(arr):
        while stack and arr[stack[-1]] < value:
            result[stack.pop()] = value
        stack.append(i)
    return result

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Next greater elements:", next_greater(arr))
