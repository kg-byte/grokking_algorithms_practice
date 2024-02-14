from chapters import read_data


def binary_search_int(item_list: list[int], item: int):
    low = 0
    high = len(item_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = item_list[mid]
        if item == guess:
            return mid
        elif item < guess:
            high = mid - 1
        else:
            low = mid + 1
    return None


def binary_search_string(item_list: list[str], item: str):
    low = 0
    high = len(item_list)
    guesses = 0
    while low <= high:
        guesses += 1
        mid = (low + high) // 2
        guess = item_list[mid]
        if guess == item:
            return mid, guesses
        elif guess < item:
            high = mid - 1
        else:
            low = mid + 1
    return None, guesses


def main():
    # test binary_search_int
    assert binary_search_int(list(range(1, 100)), 37) == 36

    # test_binary_search_str
    # maximum search 6 for 64 elements log(2)64 = 6
    # maximum search 6 for 128 elements log(2)128 = 7
    animal_names = read_data("animal_names.json")
    assert binary_search_string(animal_names[0:63], "zebra") == (None, 6)
    assert binary_search_string(animal_names[0:127], "zebra") == (None, 7)


if __name__ == "__main__":
    main()
