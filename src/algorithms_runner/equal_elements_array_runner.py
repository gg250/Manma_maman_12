from typing import List

from src.algorithms_runner.one_time_runner import OneTimeRunner

class EqualElementsArrayRunner(OneTimeRunner):
    def _create_array(self, n: int) -> List[int]:
        """
        This function creates an array which all of the elements are equal to n.
        """
        return [n] * n