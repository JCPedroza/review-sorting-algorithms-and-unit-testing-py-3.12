from random import shuffle
from timeit import default_timer as timer
from sort_types import Algorithm, AlgorithmList, IntList, Seconds


def time(algo: Algorithm, arg: IntList) -> Seconds:
    """Measures the running time of the given sorting algorithm, in seconds."""
    arg_copy = arg[:]
    start = timer()
    algo.sort(arg_copy)
    stop = timer()

    return stop - start


def time_many(algos: AlgorithmList, arg: IntList) -> dict[Algorithm, Seconds]:
    """Measures the running time of the given sorting algorithms, in seconds."""
    shuffle(algos)
    return {algo: time(algo, arg[:]) for algo in algos}


def profile(algos: AlgorithmList, arg: IntList, rep: int) -> list[tuple[str, Seconds]]:
    """Accumulates and sorts repeated running time measurements."""
    totals = {algo: 0.0 for algo in algos}

    for _ in range(rep):
        partials = time_many(algos, arg[:])
        for algo, secs in partials.items():
            totals[algo] += secs

    # Sort results in ascending order
    results = [(algo.name, total) for algo, total in totals.items()]
    results.sort(key=lambda tup: tup[1])

    return results
