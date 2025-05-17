import sys

def main(items):
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] < key:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            items = list(map(int, sys.argv[1:]))
        except ValueError:
            print("Please enter a list of integers separated by spaces.")
            sys.exit(1)
    else:
        items = [5, 2, 9, 1, 5, 6]

    print("Original array:", items)
    main(items)
    print("Sorted array (decreasing):", items)

