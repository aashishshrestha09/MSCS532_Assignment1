import sys

def main(items):
    """
    Sorts the array in-place in monotonically decreasing order using Insertion Sort.
    """
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] < key:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key

def parse_input_args():
    """
    Parses command line arguments into a list of integers.
    Returns the list or exits if invalid input is provided.
    """
    if len(sys.argv) > 1:
        try:
            return list(map(int, sys.argv[1:]))
        except ValueError:
            print("Error: Please enter a list of integers separated by spaces.")
            sys.exit(1)
    else:
        return [5, 2, 9, 1, 5, 6]

if __name__ == "__main__":
    items = parse_input_args()
    print("Original array:", items)
    main(items)
    print("Sorted array (decreasing):", items)

