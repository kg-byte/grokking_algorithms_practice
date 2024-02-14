from typing import Deque, TypeVar

# Recap
# 1. Breadth-first search tells you if there's a path from A to B.
# 2. If there's a path, breadth-first search will find the shortest path.
# 3. If you have a problem like 'find the shortest X', try modeling your problem as a grapph,
#    and use breadth-first search to solve.
# 4. A directed graph has arrows, and the relationship follows the direction of
#    the arrow (M -> P means 'M owes P money').
# 5. Undirect graphs don't have arrows and the relationship goes both ways.
#    (M - P means 'M loves P and P loves M')
# 6. Queues are FIFO (first in first out).
# 7. Stacks are LIFO (last in first out).
# 8. You need to check people in the order they were added to the search list,
#    so the search list needs to be a queue. Otherwie, you won't get the shortest path.
# 9. Once you check somone, make sure you don't check them again. Otherwise,
#    you might end up in an infinite loop. (M - P - M - P ... )

graph: dict[str, list[str]] = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


T = TypeVar("T")


class TypedDeque(Deque[T]):
    pass


def is_mango_seller(person: str):
    return person in ["joseph", "jonny"]


def find_mango_seller(start: str):
    # creates the queue
    search_queue = TypedDeque[str]()
    # keeps track of searched people
    searched: list[str] = []
    # add all of your neighbors to the search queue
    if graph.get(start):
        search_queue += graph[start]
        while search_queue:
            # grabs the first person off the queue
            person = search_queue.popleft()
            # only search this person if they haven't already been searched
            if not person in searched:
                if is_mango_seller(person):
                    print(f"{person} is a mango seller in {start}'s network!")
                    return True
                else:
                    search_queue += graph[person]
                    # marks person as searched
                    searched.append(person)
    print(f"There is no mango seller in {start}'s network")
    return False


def main():
    assert find_mango_seller("you")
    assert find_mango_seller("claire")
    assert not find_mango_seller("bob")
    assert not find_mango_seller("zac")


if __name__ == "__main__":
    main()
