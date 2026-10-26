"""Return the index where target exists or should be inserted in a sorted list."""

def search_insert(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted numbers: ").split()))
    target = int(input("Enter target: "))
    print("Insert position:", search_insert(arr, target))
