import math
import random

from typing import List

class ListCreator:
    PAIR_LETTER = 'P'
    EMPTY_PAIR_LETTER = 'E'

    @staticmethod
    def create_random_ordered_array(n: int, seed: int) -> List[int]:
        """
        This function creates a random ordered array by the size of n elemnts.
        """
        random.seed(seed)
        numbers_array = list(range(1,n+1))
        random.shuffle(numbers_array)
        return numbers_array

    @staticmethod
    def create_increasing_array(n: int) -> List[int]:
        """
        This function creates a sorted array in increasing order 
        """
        numbers_array = list(range(1,n+1))
        # This used to validate that the returned list will be sorted in increasing manner
        return sorted(numbers_array)

    @staticmethod
    def create_decreasing_array(n: int) -> List[int]:
        """
        This function creates a sorted array in decreasing order 
        """
        numbers_array = list(range(n, 0, -1))
        # This used to validate that the returned list will be sorted in decreasing manner
        return sorted(numbers_array, reverse=True)

    @staticmethod
    def create_equal_numbers_array(n: int) -> List[int]:
        """
        This function creates an array which all of the elements are equal to n.
        """
        return [n] * n

    @staticmethod
    def create_partial_sorted_array(n: int) -> List[int]:
        """
        This function creates an array which contains floor(n/20) sequential pairs shuffled.
        """
        random.seed(ListCreator.RANDOM_SEED)
        # Since we use indexes to find the start the start of each pair, the array length we use for calculations should be even
        pairs_amount = math.floor(n/20)
        pairs_order_array = ListCreator.PAIR_LETTER * pairs_amount + ListCreator.EMPTY_PAIR_LETTER * ((n/2) - pairs_amount)
        random.shuffle(pairs_order_array)
        
        # Get the pairs start indexes
        pairs_starts = [i for i, val in enumerate(pairs_order_array) if val == ListCreator.PAIR_LETTER]
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
