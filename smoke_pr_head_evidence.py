"""Format a local release-note example for the PR smoke fixture."""


def render_release_note(title: str, detail: str) -> str:
    return f"{title.strip()}: {detail.strip()}"
