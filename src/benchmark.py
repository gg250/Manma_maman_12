import tabulate
import pandas as pd
import numpy as np

from typing import Dict, List

from src.models.run_result import RunResult
from src.algorithms_runner.random_array_runner import RandomArrayRunner
from src.algorithms_runner.increasing_array_runner import IncreasingArrayRunner
from src.algorithms_runner.decreasing_array_runner import DecreasingArrayRunner
from src.algorithms_runner.equal_elements_array_runner import EqualElementsArrayRunner
from src.algorithms_runner.partial_sorted_array_runner import PartialSortedArrayRunner

ARRAY_LENGTHS = [128, 256, 512, 1024, 2048, 4096]
ALGORITHM_TYPES = ['A', 'B', 'C', 'D']
RANDOM_SEEDS = [1111, 22222, 33333, 44444, 55555]

def run_random_ordered_array_benchmark():
    table_rows = list()
    table_headers = ['Algorithm', 'Input length (n)', 'comparisons', 'writes', 'nanoseconds', 'complexity']
    array_runner = RandomArrayRunner()
    for input_length in ARRAY_LENGTHS:
        algorithms_result = array_runner.run_algorithms(input_length)
        for algorithm, run_result in algorithms_result.items():
            table_rows.append([algorithm, input_length, run_result.comparisons, run_result.writes, run_result.nanoseconds, run_result.complexity])

    print(tabulate.tabulate(table_rows, headers=table_headers, tablefmt='github')) 

def increasing_array_benchmark():
    table_rows = list()
    table_headers = ['Algorithm', 'Input length (n)', 'comparisons', 'writes', 'nanoseconds', 'complexity']
    array_runner = IncreasingArrayRunner()
    for input_length in ARRAY_LENGTHS:
        algorithms_result = array_runner.run_algorithms(input_length)
        for algorithm, run_result in algorithms_result.items():
            table_rows.append([algorithm, input_length, run_result.comparisons, run_result.writes, run_result.nanoseconds, run_result.complexity])

    print(tabulate.tabulate(table_rows, headers=table_headers, tablefmt='github')) 

def decreasing_array_benchmark():
    table_rows = list()
    table_headers = ['Algorithm', 'Input length (n)', 'comparisons', 'writes', 'nanoseconds', 'complexity']
    array_runner = DecreasingArrayRunner()
    for input_length in ARRAY_LENGTHS:
        algorithms_result = array_runner.run_algorithms(input_length)
        for algorithm, run_result in algorithms_result.items():
            table_rows.append([algorithm, input_length, run_result.comparisons, run_result.writes, run_result.nanoseconds, run_result.complexity])

    print(tabulate.tabulate(table_rows, headers=table_headers, tablefmt='github')) 

def equal_elements_array_benchmark():
    table_rows = list()
    table_headers = ['Algorithm', 'Input length (n)', 'comparisons', 'writes', 'nanoseconds', 'complexity']
    array_runner = EqualElementsArrayRunner()
    for input_length in ARRAY_LENGTHS:
        algorithms_result = array_runner.run_algorithms(input_length)
        for algorithm, run_result in algorithms_result.items():
            table_rows.append([algorithm, input_length, run_result.comparisons, run_result.writes, run_result.nanoseconds, run_result.complexity])

    print(tabulate.tabulate(table_rows, headers=table_headers, tablefmt='github')) 

def equal_elements_array_benchmark():
    table_rows = list()
    table_headers = ['Algorithm', 'Input length (n)', 'comparisons', 'writes', 'nanoseconds', 'complexity']
    array_runner = EqualElementsArrayRunner()
    for input_length in ARRAY_LENGTHS:
        algorithms_result = array_runner.run_algorithms(input_length)
        for algorithm, run_result in algorithms_result.items():
            table_rows.append([algorithm, input_length, run_result.comparisons, run_result.writes, run_result.nanoseconds, run_result.complexity])

    print(tabulate.tabulate(table_rows, headers=table_headers, tablefmt='github'))

def partial_sorted_array_benchmark():
    table_headers = ['Algorithm', 'Input length (n)', 'comparisons', 'writes', 'nanoseconds', 'C(n)']
    array_runner = PartialSortedArrayRunner()
    table_rows = list()
    for input_length in ARRAY_LENGTHS:
        algorithms_result = array_runner.run_algorithms(input_length)
        table_rows.extend(convert_run_result_to_rows(algorithms_result, input_length))

    table_rows_for_2n = list()
    for input_length in np.array(ARRAY_LENGTHS) * 2:
        algorithms_result = array_runner.run_algorithms(input_length * 2)
        table_rows_for_2n.extend(convert_run_result_to_rows(algorithms_result, input_length))
    

    results = pd.DataFrame(table_rows, columns=table_headers)
    results_for_2n = pd.DataFrame(table_rows_for_2n, columns=table_headers)
    results['C(2n)/C(n)'] = results_for_2n['C(n)'] / results['C(n)']

    print(results)

def convert_run_result_to_rows(algorithms_result: Dict[str, RunResult], input_length: int) -> List[List[int]]:
    rows = list()
    for algorithm, run_result in algorithms_result.items():
                rows.append([algorithm, input_length, run_result.comparisons, run_result.writes, run_result.nanoseconds, run_result.complexity])

    return rows

if __name__ == '__main__':
    partial_sorted_array_benchmark()