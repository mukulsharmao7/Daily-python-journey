# def average_loop(numbers: list[float]) -> float:
#     """Return the average using a for loop, or 0.0 if the list is empty."""
#     if not numbers:
#         return 0.0
#     total = 0
#     for number in numbers:
#         total += number
#     return total / len(numbers)


# print(average_loop([1, 2, 3]))
# print(average_loop([10.5, 20.5]))
# print(average_loop([]))
# print(average_loop("hello"))   # TypeError: unsupported operand type(s) for +=: 'int' and 'str'

# def average_validated(numbers: list[float]) -> float:
#     """Return the average of a list of numbers.

#     Raises TypeError if input is not a list or has non-numeric elements.
#     Returns 0.0 for an empty list.
#     """
#     if not isinstance(numbers, list):
#         raise TypeError("numbers must be a list")
#     for number in numbers:
#         if not isinstance(number, (int, float)):
#             raise TypeError("all elements must be numbers")
#     if not numbers:
#         return 0.0
#     return sum(numbers) / len(numbers)


# for data in ([1, 2, 3], "hello", [1, "a", 3]):
#     try:
#         print(average_validated(data))
#     except TypeError as e:
#         print("Error:", e)
        
        
def safe_divide(a: float, b: float) -> float:
    """Return a / b.

    Raises TypeError if a or b is not a number.
    Raises ValueError if b is zero.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numbers")
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b


for a, b in [(10, 2), ("10", 2), (10, 0)]:
    try:
        print(safe_divide(a, b))
    except TypeError as e:
        print("TypeError:", e)
    except ValueError as e:
        print("ValueError:", e)