def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    return n % 2 == 0


assert is_even(2), "is_even(2) should be True"
assert is_even(0), "is_even(0) should be True"
assert is_even(-4), "is_even(-4) should be True"
assert not is_even(3), "is_even(3) should be False"

print("All tests passed")

assert is_even(3), "is_even(3) should be False, so this test must fail"