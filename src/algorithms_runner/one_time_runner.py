from typing import Dict, List
from statistics import mean

from algorithms_runner.algorithms_runner import AlgorithmsRunner
from src.models.run_result import RunResult
from src.black_box import run

class OneTimeRunner(AlgorithmsRunner):
    def run_algorithms(self, input_length: int) -> Dict[str, RunResult]:
            run_results = dict()
            for algorithm_type in self.ALGORITHM_TYPES:
                run_results.update({algorithm_type: self.run_algorithm(algorithm_type, input_length)})
    
            return run_results

    def _run_algorithm(self, algorithm_type: str, input_length: int) -> RunResult:
        input = self._create_array(input_length)
        result = run(algorithm_type, input)
        return RunResult(
                        comparisons=result.comparisons,
                        writes=result.writes,
                        nanoseconds=result.nanoseconds
                    )         

    def _create_array(self, n: int) -> List[int]:
        raise NotImplementedError()