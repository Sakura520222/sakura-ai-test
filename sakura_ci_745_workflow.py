"""Small count helper for the Sakura-AI workflow-run integration check."""

def accepted_count(requested: int, capacity: int) -> int:
    """Return the count clamped to the inclusive range from zero to capacity."""
    return max(0, min(requested, capacity))
