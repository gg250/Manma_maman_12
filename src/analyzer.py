import numpy as np
import pandas as pd

class Analyzer:
    @staticmethod
    def analyze_complexity(original_results: pd.DataFrame, results_for_2n: pd.DataFrame) -> pd.DataFrame:
        results = original_results.copy()
        results['C(2n)/C(n)'] = results_for_2n['C(n)'] / original_results['C(n)']
        input_length = original_results['Input length (n)']
        results['C(n)/n'] = original_results['C(n)'] / input_length
        results['C(n)/nlog(n)'] = original_results['C(n)'] / (input_length * np.log2(input_length))
        results['C(n)/(n^2)'] = original_results['C(n)'] / np.power(input_length, 2)
        return results

    @staticmethod
    def analyze_writes(original_results: pd.DataFrame, results_for_2n: pd.DataFrame) -> pd.DataFrame:
        results = original_results.copy()
        results['writes (2n)/ writes (n)'] = results_for_2n['writes'] / original_results['writes']
        input_length = original_results['Input length (n)']
        results['writes (n)/n'] = original_results['writes'] / input_length
        results['writes (n)/nlog(n)'] = original_results['writes'] / (input_length * np.log2(input_length))
        results['writes (n)/(n^2)'] = original_results['writes'] / np.power(input_length, 2)
        return results

    @staticmethod
    def analyze_comparisons(original_results: pd.DataFrame, results_for_2n: pd.DataFrame) -> pd.DataFrame:
        results = original_results.copy()
        results['comparisons (2n)/ comparisons (n)'] = results_for_2n['comparisons'] / original_results['comparisons']
        input_length = original_results['Input length (n)']
        results['comparisons (n)/n'] = original_results['comparisons'] / input_length
        results['comparisons (n)/nlog(n)'] = original_results['comparisons'] / (input_length * np.log2(input_length))
        results['comparisons (n)/(n^2)'] = original_results['comparisons'] / np.power(input_length, 2)
        return results