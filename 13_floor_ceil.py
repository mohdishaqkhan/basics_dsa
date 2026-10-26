"""Find floor and ceil of a value in a sorted array."""

def floor_ceil(arr, x):
    floor_value = None
    ceil_value = None
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return arr[mid], arr[mid]
        if arr[mid] < x:
            floor_value = arr[mid]
            left = mid + 1
        else:
            ceil_value = arr[mid]
            right = mid - 1
    return floor_value, ceil_value

if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted numbers: ").split()))
    x = int(input("Enter value: "))
    floor_value, ceil_value = floor_ceil(arr, x)
    print("Floor:", floor_value)
    print("Ceil:", ceil_value)
