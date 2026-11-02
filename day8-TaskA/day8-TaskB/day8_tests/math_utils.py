def safe_divide(a: float, b: float) -> float:
    """Return a / b. Raise TypeError for non-numbers, ValueError if b is zero."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numbers")
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b