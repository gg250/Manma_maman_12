import random
import math

from src.algorithm_runner.random_array_runner import RandomArrayRunner

class PartialSortedArrayRunner(RandomArrayRunner):
    PAIR_LETTER = 'P'
    EMPTY_PAIR_LETTER = 'E'
    
    def _create_array(n, seed):
        """
        This function creates an array which contains floor(n/20) sequential pairs shuffled.
        """
        random.seed(seed)
        # Since we use indexes to find the start the start of each pair, the array length we use for calculations should be even
        pairs_amount = math.floor(n/20)
        pairs_order_array = PartialSortedArrayRunner.PAIR_LETTER * pairs_amount + PartialSortedArrayRunner.EMPTY_PAIR_LETTER * ((n/2) - pairs_amount)
        random.shuffle(pairs_order_array)
        
        # Get the pairs start indexes
        pairs_starts = [i for i, val in enumerate(pairs_order_array) if val == PartialSortedArrayRunner.PAIR_LETTER]
        # Create a numbers array in the size of n
        numbers_array = range(1, n+1)
        
        # Get the pairs values from the values array itself
        pairs = [(numbers_array[i], numbers_array[i+1]) for i in pairs_starts]
        random.shuffle(pairs)
        
        # Put back the shuffled pairs into the numbers array
        for i, (first_value, second_value) in zip(pairs_starts, pairs):
            numbers_array[i] = first_value
            numbers_array[i+1] = second_value

        return numbers_array