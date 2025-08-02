from pathlib import Path
from typing import Any

class Image:
    path: Path
    width: int
    height: int

    def __init__(self, path: str | Path) -> None: ...
    def crop(self, x: int, y: int, width: int, height: int) -> Image: ...
    def save(self, path: str | Path) -> None: ...

# Module export
image_cropper: Any