def safe_divide(a: float, b: float) -> float:
    """Return a / b. Raise TypeError for non-numbers, ValueError if b is zero."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numbers")
    if b ==0:
        raise ValueError(" b should not be equal to 0 ")
        
    return a / b
    


# Normal tests
assert safe_divide(10, 2) == 5.0, "safe_divide(10, 2) should be 5.0"
assert safe_divide(7, 2) == 3.5, "safe_divide(7, 2) should be 3.5"
assert safe_divide(0, 5) == 0.0, "safe_divide(0, 5) should be 0.0"

# Error test 1: zero par ValueError aana chahiye
try:
    safe_divide(10, 0)
    assert False, "ValueError should have been raised for b = 0"
except ValueError:
    pass

# Error test 2: string par TypeError aana chahiye
try:
    safe_divide("10", 2)
    assert False, "TypeError should have been raised for a = '10'"
except TypeError:
    pass

print("All tests passed")