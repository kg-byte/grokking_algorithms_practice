from time import perf_counter, sleep

# Recap
# Hashes are good for
# 1. Modeling relationships from one thing to another thing.
# 2. Filtering out duplicates.
# 3. Caching/memorizing data instead of making your server do work.

# You'll almost never have to implement a hash table yourself and assume that you'll
# get the average case performance: constant time using the built in hash.
# Hash tables are powerful data structure because they're so fast and they let you model
# data in a different way. You might soon find that you're using them all the time:
# 1. You can make a hash table by combining a hash function with an array,
# 2. Collisions are bad. Yopu need a hash function that minimizes collisions.
# 3. Hash tables have really fast search, insert, and delete.
# 4. Hash tables are good for modeling relationships from one item to another.
# 5. Once your load factor is greater than 0.7, it's time to resize your hash table.
# 6. Hash tables are used for caching data.
# 7. Hash tables are great for catching duplicates.


# average hash table O(1), worse case O(n) in search, inserts & deletes
# collisions causes worst scenario; to avoid collision, we need:
# 1. A low load factor: number of items in hash table/ total number of slots
#    once a load factor grows bigger (> 0.7) -> resizing(double the size)
# 2. A good hash function: distributes values in the array evenly and avoids collision


# Exercises
# It's important for hash functions to have good distribution. They should map items
# as broadly as possible. The worst case is a hash function tht maps all items to the same slot
# in the hash table.
# Suppose you have these four hash functions that wrok with strings
# A. Return "1" for all input
# B. Use the length of the string as the index
# C. Use the first caracter of the string as the index, so all strings starting with a
#    are hashed together, and so on
# D. Map every letter to a prime number, a = 2, b = 3, c = 5, d = 7, e = 11...
#    for a string, the hash function is the sum of all the characters modulo the size of the hash.
#    If your hash size is 10, and string is 'bag', the index is 3+2+17 = 22 %10 = 2
# For each of these following examples, which hash functions would provide a good distribution?
# Assume hash table size is 10 slots.
# 1. A phone book where the keys are names and values are phone numbers.
#    The names are: Esther, Ben, Bob, and Dan. (C & D)
# 2. A mapping from battery size to powerw. The sizes are A, AA, AAA, AAAA. (B & D)
# 3. A mapping from book titles to authors. The authors are Maus, Fun home, and Watchman(B, C & D)
cache: dict[str, str] = {}


def get_data_from_server(url: str):
    sleep(1)
    return f"here's the content for url '/{url}'"


def get_page(url: str):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data


def performance_counter(url: str):
    time_before = perf_counter()
    print(get_page(url))
    print(f"It took {perf_counter() - time_before} seconds to get {url} page")



def main():
    # performance_counter("about")
    # performance_counter("about")


if __name__ == "__main__":
    main()
