from typing import List

from src.algorithms_runner.one_time_runner import OneTimeRunner

class DecreasingArrayRunner(OneTimeRunner):
    def _create_array(self, n: int) -> List[int]:
        """
        This function creates a sorted array in decreasing order 
        """
        numbers_array = list(range(n, 0, -1))
        # This used to validate that the returned list will be sorted in decreasing manner
        return sorted(numbers_array, reverse=True)