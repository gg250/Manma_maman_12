from dataclasses import dataclass

@dataclass
class RunResult:
    comparisons: int
    writes: int
    nanoseconds: int

    @property
    def complexity() -> str:
        pass
