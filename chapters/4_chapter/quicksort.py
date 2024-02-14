# Recap
# 1. D&C works by breaking a problem down into smaller and smaller
#    pieces. If you're using D&C on a list, the base case is probably an
#    empty array or an array with one element.
# 2. If you're implementing quicksort, choose a random element as the pivot.
#    The average runtime of quicksort is O(n log n)!
# 3. The constant in Big O notation can matter sometimes. That's why
#    quicksort is faster than merge sort.
# 4. The constant almost never matters for simple search vs binary search,
#    because O(log n) is so much faster than O(n) when your list gets big.


# Exercises:
# How long would each of these operations take in Big O notation?
# 1. printing the value of each element in an array. O(n)
# 2. doubling the value of each element in an array. O(n)
# 3. doubling the value of just the first element in an array. O(1)
# 4. Creating multiplication table with all elements in the array.
#    if your array is [2, 3, 7, 8, 10], first multiply every element
#    by 2, then multiply every element by 3, then by 7, and so on. O(n2)


def quicksort(arr: list[int]) -> list[int]:
    # base case
    if len(arr) < 2:
        return arr
    # recursive case
    else:
        pivot = arr[0]
        less = [i for i in arr if i < pivot]
        greater = [i for i in arr if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


def main():
    assert quicksort([10, 5, 2, 3]) == [2, 3, 5, 10]


if __name__ == "__main__":
    main()
