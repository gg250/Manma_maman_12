import tabulate
import pandas as pd
import numpy as np

from typing import Dict, List

from src.models.run_result import RunResult
from src.algorithms_runner.algorithms_runner import AlgorithmsRunner
from src.algorithms_runner.random_array_runner import RandomArrayRunner
from src.algorithms_runner.increasing_array_runner import IncreasingArrayRunner
from src.algorithms_runner.decreasing_array_runner import DecreasingArrayRunner
from src.algorithms_runner.equal_elements_array_runner import EqualElementsArrayRunner
from src.algorithms_runner.partial_sorted_array_runner import PartialSortedArrayRunner
from src.analyzer import Analyzer

ARRAY_LENGTHS = [128, 256, 512, 1024, 2048, 4096]
ALGORITHM_TYPES = ['A', 'B', 'C', 'D']
RANDOM_SEEDS = [1111, 22222, 33333, 44444, 55555]

def write_results_to_excel() -> None:
    random_array_results = run_random_ordered_array_benchmark()
    increasing_array_results = increasing_array_benchmark()
    decreasing_array_results = decreasing_array_benchmark()
    equal_elements_array_results = equal_elements_array_benchmark()
    partial_sorted_array_results = partial_sorted_array_benchmark()
    with pd.ExcelWriter('results/results.xlsx', engine='openpyxl') as writer:
        random_array_results.to_excel(writer, sheet_name='random_ordered_array', index=False)
        increasing_array_results.to_excel(writer, sheet_name='increasing_array', index=False)
        decreasing_array_results.to_excel(writer, sheet_name='decreasing_array', index=False)
        equal_elements_array_results.to_excel(writer, sheet_name='equal_elements_array', index=False)
        partial_sorted_array_results.to_excel(writer, sheet_name='partial_sorted_array', index=False)

def run_random_ordered_array_benchmark() -> pd.DataFrame:
    array_runner = RandomArrayRunner()
    results_for_n = run_benchmark(array_runner, ARRAY_LENGTHS)
    results_for_2n = run_benchmark(array_runner, list(np.array(ARRAY_LENGTHS) * 2))
    return analyze_results(results_for_n, results_for_2n)

def increasing_array_benchmark():
    array_runner = IncreasingArrayRunner()
    results_for_n = run_benchmark(array_runner, ARRAY_LENGTHS)
    results_for_2n = run_benchmark(array_runner, list(np.array(ARRAY_LENGTHS) * 2))
    return analyze_results(results_for_n, results_for_2n)

def decreasing_array_benchmark():
    array_runner = DecreasingArrayRunner()
    results_for_n = run_benchmark(array_runner, ARRAY_LENGTHS)
    results_for_2n = run_benchmark(array_runner, list(np.array(ARRAY_LENGTHS) * 2))
    return analyze_results(results_for_n, results_for_2n)

def equal_elements_array_benchmark():
    array_runner = EqualElementsArrayRunner()
    results_for_n = run_benchmark(array_runner, ARRAY_LENGTHS)
    results_for_2n = run_benchmark(array_runner, list(np.array(ARRAY_LENGTHS) * 2))
    return analyze_results(results_for_n, results_for_2n)

def partial_sorted_array_benchmark() -> pd.DataFrame:
    array_runner = PartialSortedArrayRunner()
    results_for_n = run_benchmark(array_runner, ARRAY_LENGTHS)
    results_for_2n = run_benchmark(array_runner, list(np.array(ARRAY_LENGTHS) * 2))
    return analyze_results(results_for_n, results_for_2n)

def run_benchmark(algorithm_runner: AlgorithmsRunner, input_lengths: List[int]) -> pd.DataFrame:
    table_headers = ['Algorithm', 'Input length (n)', 'comparisons', 'writes', 'nanoseconds', 'C(n)']
    table_rows = list()
    for input_length in input_lengths:
        algorithms_result = algorithm_runner.run_algorithms(input_length)
        table_rows.extend(convert_run_result_to_rows(algorithms_result, input_length))

    return pd.DataFrame(table_rows, columns=table_headers)

def analyze_results(results_for_n: pd.DataFrame, results_for_2n: pd.DataFrame) -> pd.DataFrame:
    analyzed_results = Analyzer.analyze_complexity(results_for_n, results_for_2n)
    analyzed_results = Analyzer.analyze_comparisons(analyzed_results, results_for_2n)
    analyzed_results = Analyzer.analyze_writes(analyzed_results, results_for_2n)
    return analyzed_results

def convert_run_result_to_rows(algorithms_result: Dict[str, RunResult], input_length: int) -> List[List[int]]:
    rows = list()
    for algorithm, run_result in algorithms_result.items():
                rows.append([algorithm, input_length, run_result.comparisons, run_result.writes, run_result.nanoseconds, run_result.complexity])

    return rows
    

if __name__ == '__main__':
    write_results_to_excel()
    # results = increasing_array_benchmark()
    # print(results)