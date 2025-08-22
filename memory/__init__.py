import pickle
from pathlib import Path
from typing import Any, Dict

class Memory:
    """Binary long-term memory storage.

    Data is serialized via pickle into a binary file so it is not
    human-readable.  The memory loads itself on creation and saves on
    every update.
    """

    def __init__(self, path: Path):
        self.path = path
        self.data: Dict[str, Any] = {}
        self.load()

    def load(self) -> None:
        if self.path.exists():
            with self.path.open("rb") as f:
                self.data = pickle.load(f)

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("wb") as f:
            pickle.dump(self.data, f)

    def remember(self, key: str, value: Any) -> None:
        self.data[key] = value
        self.save()

    def recall(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)
