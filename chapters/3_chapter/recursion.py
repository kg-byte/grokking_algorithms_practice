# Recap
# 1. Recusion is when a function calls itself.
# 2. Every recursive function has two cases: the base case and the recursive case.
# 3. A stack has two operations: push and pop.
# 4. All function calls go onto the call stack.
# 5. The call stack can get very large, which takes a lot of memory.
# Bonus: Each program has a limited amount of space on the call stack. When your program runs out of space,
#        (which it eventually will), it will exist with a stack-overflow error.


# key problem
#   Loops may achieve a performance gain for your program. Recusion may achieve a performance gain for your programmer.
#   Choose which is more important in your situation! - Leigh Caldwell
# def look_for_key_while_loop(box):
#     pile = main_box.make_a_pile_to_look_through()
#     while pile is not empty:
#         for item in box:
#             if item.is_a_box():
#                 pile.append(item)
#             elif item.is_a_key):
#                 print('found the key!')
# def look_for_key_recursive(box):
#     for item in box:
#         if item.is_a_box():
#             look_for_key_recursive(item)
#         elif item.is_a_key():
#             print("found the key!")


def countdown(i: int) -> None:
    print(i)
    # base case
    if i <= 1:
        return
    # recursive case
    else:
        countdown(i - 1)


# Tail-call Optimization/Elimination
# Recursion is called tail-recursive when the recursive call is the last thing executed by the method.
# only linear recursion can be transformed into tail_recursion, e.g. Countdown.
# If the recursive call is not the last thing executed, it is head-recursion.
# tail recursion reduces memory complexity from O(n) -> O(1)
# because there is no need to preserve the stack frames for previous calls


def factorial_recursive_head(i: int) -> int:
    if i == 1:
        return i
    else:
        return i * factorial_recursive_head(i - 1)


def factorial_recursive_tail(n: int) -> int:
    return _factorial_recursive_tail(n, 1)


def _factorial_recursive_tail(n: int, x: int) -> int:
    if n == 1:
        return x
    return _factorial_recursive_tail(n - 1, n * x)


def fibonacci_recursive_head(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive_head(n - 1) + fibonacci_recursive_head(n - 2)


def fibonacci_recursive_tail(n: int) -> int:
    return _fibonacci_recursive_tail(n, 0, 1)


def _fibonacci_recursive_tail(n: int, a: int, b: int) -> int:
    if n == 0:
        return a
    if n == 1:
        return b
    return _fibonacci_recursive_tail(n - 1, b, a + b)


def main():
    countdown(10)
    assert factorial_recursive_head(5) == 120
    assert factorial_recursive_tail(5) == 120
    assert fibonacci_recursive_head(6) == 8
    assert fibonacci_recursive_tail(6) == 8


if __name__ == "__main__":
    main()
