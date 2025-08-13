from dataclasses import dataclass
from pathlib import Path

@dataclass
class Track:
    id: str
    title: str
    artist: str
    album: str
    duration: float | None
    full_path: Path | str
