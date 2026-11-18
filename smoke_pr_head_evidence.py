"""Format a local release-note example for the PR smoke fixture."""


def clean_release_line(text: str) -> str:
    """Remove repeated spaces and line breaks from one line."""

    return " ".join(text.split())


def render_release_note(title: str, detail: str) -> str:
    normalized_title = clean_release_line(title)
    normalized_detail = clean_release_line(detail)
    if not normalized_title:
        normalized_title = "Update"
    if not normalized_detail:
        return normalized_title
    return f"{normalized_title}: {normalized_detail}"


def release_state_label() -> str:
    return "ready for a committed review"
