from dataclasses import dataclass
from pathlib import Path

@dataclass
class Track:
    id: str
    title: str
    artist: str
    album: str
    duration: int
    full_path: Path | str
