from typing import Callable, List, Any

class Router:
    """Simple in-memory message router."""

    def __init__(self) -> None:
        self.handlers: List[Callable[[Any], None]] = []

    def connect(self, handler: Callable[[Any], None]) -> None:
        self.handlers.append(handler)

    def broadcast(self, message: Any) -> None:
        for h in self.handlers:
            h(message)
