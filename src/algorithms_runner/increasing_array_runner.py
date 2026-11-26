from typing import List

from src.algorithms_runner.one_time_runner import OneTimeRunner

class IncreasingArrayRunner(OneTimeRunner):
    def _create_array(self, n: int) -> List[int]:
        """
        This function creates a sorted array in increasing order 
        """
        numbers_array = list(range(1,n+1))
        # This used to validate that the returned list will be sorted in increasing manner
        return sorted(numbers_array)