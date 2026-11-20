from black_box import run
from list_creator import ListCreator

ARRAY_LENGTHS = [128, 256, 512, 1024, 2048, 4096]
ALGORITHM_TYPES = ['A', 'B', 'C', 'D']
RANDOM_SEEDS = [1111, 22222, 33333, 44444, 55555]

def run_random_ordered_array_benchmark():
    for algorithm_type in ALGORITHM_TYPES:
        execution_times = list()
        for random_seed in RANDOM_SEEDS:
            data_array = ListCreator.create_random_ordered_array()
            result = run(algorithm_type, data_array)
            execution_times.append()

def calculate_random_ordered_array_parameters(algorithm_type: str, array_length: int) -> dict:
