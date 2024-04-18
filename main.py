from random import randrange
from sort_time import profile
from sort_repo import algorithms


def main():
    SIZE = 100
    REP = 5
    ints = [randrange(-999, 1000) for _ in range(SIZE)]
    results = profile(algorithms, ints, REP)

    max_name_len = 0
    for res in results:
        if len(res[0]) > max_name_len:
            max_name_len = len(res[0])

    logs = [(res[0].ljust(max_name_len + 1), round(res[1], 7)) for res in results]

    for log in logs:
        print(f"{log[0]}: {log[1]}s")


if __name__ == "__main__":
    main()
