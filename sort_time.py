from random import shuffle
from timeit import default_timer as timer
from sort_types import FloatSeconds, IntList, SortingAlgorithm, SortingAlgorithmList
from sort_repo import algorithms


def time(algo: SortingAlgorithm, arg: IntList) -> FloatSeconds:
    """Measures the running time of the given sorting algorithm, in seconds."""
    start = timer()
    algo.sort(arg)
    stop = timer()

    return stop - start


def time_many(algos: SortingAlgorithmList, arg: IntList):
    """Measures the running time of the given sorting algorithms, in seconds."""
    shuffle(algos)
    return {algo: time(algo, arg) for algo in algos}


def profile(algos: SortingAlgorithmList, arg: IntList, reps: int):
    totals = {algo: 0 for algo in algos}

    for _ in range(reps):
        partials = time_many(algos, arg)
        for algo, secs in partials.items():
            totals[algo] += secs

    # Sort results in ascending order
    results = [(algo.name, total) for algo, total in totals.items()]
    results.sort(key = lambda tup: tup[1])

    return results
