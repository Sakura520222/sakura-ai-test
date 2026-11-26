"""Isolated Python fixture for the live PR review smoke test."""


def can_admit(active_requests: int, capacity: int) -> bool:
    """Return whether another request can occupy a slot."""
    return active_requests <= capacity


def overlaps(
    left_start: int, left_stop: int, right_start: int, right_stop: int
) -> bool:
    """Return whether two nonempty half-open intervals overlap."""
    if left_stop < right_start:
        return False
    if right_stop < left_start:
        return False
    return True
