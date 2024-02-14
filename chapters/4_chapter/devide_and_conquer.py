# sum of an array
def sum_loop(arr: list[int]) -> int:
    total = 0
    for i in arr:
        total += i
    return total


def sum_devide_and_conquer(arr: list[int]) -> int:
    # first find basecase
    if len(arr) == 0:
        return 0
    # reduce problem until base case is met
    else:
        return arr[0] + sum_devide_and_conquer(arr[1:])


def _sum_recursive_tail(arr: list[int], sum: int) -> int:
    if len(arr) == 0:
        return sum
    else:
        sum += arr[0]
        return _sum_recursive_tail(arr[1:], sum)


def sum_recursive_tail(arr: list[int]) -> int:
    return _sum_recursive_tail(arr, 0)


def count_recursive(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0
    else:
        return 1 + count_recursive(arr[1:])


def max_recursive(arr: list[int]) -> int:
    # base case
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    else:
        sub_max = max_recursive(arr[1:])
        return arr[0] if arr[0] > sub_max else sub_max


def binary_search_int_recursive(arr: list[int], item: int) -> bool:
    mid = (0 + len(arr)) // 2
    # base case
    if len(arr) == 1:
        return arr[0] == item
    elif arr[mid] == item:
        return True
    elif arr[mid] < item:
        return binary_search_int_recursive(arr[mid + 1 :], item)
    else:
        return binary_search_int_recursive(arr[: mid - 1], item)


def main():
    arr = [1, 2, 3, 4]
    assert sum_loop(arr) == 10
    assert sum_devide_and_conquer(arr) == 10
    assert sum_recursive_tail(arr) == 10
    assert count_recursive(arr) == 4
    assert max_recursive(arr) == 4
    assert binary_search_int_recursive(arr, 3)
    assert not binary_search_int_recursive(arr, 8)


if __name__ == "__main__":
    main()
