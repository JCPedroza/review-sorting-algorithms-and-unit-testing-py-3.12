from sys import argv
from random import randrange
from sort_time import profile
from sort_repo import algorithms

SIZE = 500
REPE = 20

ERR_LEN = "Provide either zero or two arguments, using default values"
ERR_SIZE = "is not a valid list size, using default value"
ERR_REPE = "is not a valid number of repetitions, using default value"


def get_cli_args():
    size = SIZE
    repe = REPE

    if len(argv) not in (1, 3):
        print(ERR_LEN)
    elif len(argv) == 3:
        if argv[1].isdigit():
            size = int(argv[1])
        else:
            print(f"'{argv[1]}' {ERR_SIZE}")
        if argv[2].isdigit():
            repe = int(argv[2])
        else:
            print(f"'{argv[2]}' {ERR_REPE}")

    print(f"\nRunning with\n  list size = {size}\n  repetitions = {repe}\n")
    return size, repe


def main():
    size, repe = get_cli_args()

    ints = [randrange(-9999, 10000) for _ in range(size)]
    results = profile(algorithms, ints, repe)

    pad = 0
    for res in results:
        if len(res[0]) > pad:
            pad = len(res[0])

    logs = [(res[0].ljust(pad + 1), round(res[1], 7)) for res in results]

    for log in logs:
        print(f"{log[0]}: {log[1]}s")
    print()


if __name__ == "__main__":
    main()
