import tabulate

from src.algorithms_runner.random_array_runner import RandomArrayRunner

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


if __name__ == '__main__':
    run_random_ordered_array_benchmark()