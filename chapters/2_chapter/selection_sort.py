# Recap
# 1. Your computer's memory is like a giant set of drawers.
# 2. When you want to store multiple elements, use an array or a list.
# 3. With an array, all your elements are sorted right next to each other (contiguously)
# 4. With a list, elements are strewn all over, and one element stores the address of the next one.
# 5. Arrays allow fast reads.
# 6. Linked lists allow fast inserts and deletes.
# 7. All elements in the array should be the same type (all ints, all doubles, and so on).


def find_smallest_index(data_list: list[int]) -> int:
    smallest = data_list[0]
    smallest_index = 0

    for i, v in enumerate(data_list):
        if v < smallest:
            smallest = v
            smallest_index = i
    return smallest_index


def selection_sort(data_list: list[int]) -> list[int]:
    sorted_list: list[int] = []
    while len(data_list) > 0:
        smallest_index = find_smallest_index(data_list)
        sorted_list.append(data_list.pop(smallest_index))
    return sorted_list


def main():
    data = [2, 8, 7, 10, 44, 1, 20]
    assert find_smallest_index(data) == 5
    assert selection_sort(data) == [1, 2, 7, 8, 10, 20, 44]


if __name__ == "__main__":
    main()
