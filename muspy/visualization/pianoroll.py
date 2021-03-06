"""Piano-roll visualization interface."""
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ..music import Music


def show_pianoroll(music: "Music", **kwargs: Any):
    """Show pianoroll visualization."""
    m = music.to_pypianoroll()
    return m.plot(**kwargs)
