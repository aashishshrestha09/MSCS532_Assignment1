def main(items):
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] < key:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key


if __name__ == "__main__":
    items = [5, 2, 9, 1, 5, 6]
    print("Original array:", items)
    main(items)
    print("Sorted array (decreasing):", items)

