class Engine:
    """Handles planning, dreaming and simulation stubs."""

    def __init__(self) -> None:
        self.log = []

    def plan(self, goal: str) -> None:
        self.log.append(f"planning for {goal}")

    def dream(self) -> str:
        return "fragments of electric sheep"
