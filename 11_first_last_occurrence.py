"""Find the first and last occurrence in a sorted array using binary search."""

def first_occurrence(arr, target):
    left, right, answer = 0, len(arr) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            answer = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return answer

def last_occurrence(arr, target):
    left, right, answer = 0, len(arr) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            answer = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return answer

if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted numbers: ").split()))
    target = int(input("Enter target: "))
    print("First index:", first_occurrence(arr, target))
    print("Last index:", last_occurrence(arr, target))
