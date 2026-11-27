def clamp_quantity(quantity: int, capacity: int) -> int:
    """Clamp quantity to the interval from zero to the nonnegative capacity."""
    return min(quantity, capacity)
