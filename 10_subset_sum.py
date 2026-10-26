"""Check whether any subset of the list adds up to target."""

def subset_sum(arr, target, index=0):
    if target == 0:
        return True
    if index == len(arr):
        return False
    return (subset_sum(arr, target - arr[index], index + 1)
            or subset_sum(arr, target, index + 1))

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    target = int(input("Enter target sum: "))
    print("Subset exists" if subset_sum(arr, target) else "No subset found")
