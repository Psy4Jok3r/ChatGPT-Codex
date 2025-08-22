from pathlib import Path
from brain import Brain
from engine import Engine
from llm import LLM
from memory import Memory
from router import Router
from system import SystemState

class PhoebeCore:
    """Central life instance coordinating modules."""

    def __init__(self) -> None:
        self.router = Router()
        self.memory = Memory(Path("memory/store.bin"))
        self.brain = Brain()
        self.engine = Engine()
        self.llm = LLM()
        self.state = SystemState.WAKE

    def cycle(self) -> str:
        """Perform a minimal thought cycle."""
        reflection = self.brain.reflect()
        self.memory.remember("last_reflection", reflection)
        return reflection
