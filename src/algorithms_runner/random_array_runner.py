import random

from typing import Dict, List
from statistics import mean

from src.models.run_result import RunResult
from src.algorithms_runner.algorithms_runner import AlgorithmsRunner
from src.black_box import run

class RandomArrayRunner(AlgorithmsRunner):
    def __init__(self):
        super().__init__()
        self._random_seeds = [1111, 22222, 33333, 44444, 55555]

    def run_algorithms(self, input_length: int) -> Dict[str, RunResult]:
        run_results = dict()
        for algorithm_type in self.ALGORITHM_TYPES:
            run_results.update({algorithm_type: self._run_algorithm(algorithm_type, input_length)})

        return run_results

    def _run_algorithm(self, algorithm_type: str, input_length: int) -> RunResult:
            run_results = list()
            
            for seed in self._random_seeds:
                input = self._create_array(input_length, seed)
                result = run(algorithm_type, input)
                run_results.append(result)

            return RunResult(
                comparisons=mean(result.comparisons for result in run_results),
                writes=mean(result.writes for result in run_results),
                nanoseconds=mean(result.nanoseconds for result in run_results)
            )

    def _create_array(self, n: int, seed: int) -> List[int]:
            """
            This function creates a random ordered array by the size of n elemnts.
            """
            random.seed(seed)
            numbers_array = list(range(1,n+1))
            random.shuffle(numbers_array)
            return numbers_array