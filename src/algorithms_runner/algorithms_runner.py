from typing import Dict
from src.models.run_result import RunResult


class AlgorithmsRunner:
    ALGORITHM_TYPES = ['A', 'B', 'C', 'D']

    def run_algorithms(self, input_length: int) -> Dict[str, RunResult]:
        raise NotImplementedError()