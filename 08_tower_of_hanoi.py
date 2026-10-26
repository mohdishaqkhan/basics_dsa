"""Solve Tower of Hanoi recursively."""

def tower_of_hanoi(n, source, auxiliary, destination):
    if n <= 0:
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)

if __name__ == "__main__":
    n = int(input("Enter number of disks: "))
    tower_of_hanoi(n, "A", "B", "C")
