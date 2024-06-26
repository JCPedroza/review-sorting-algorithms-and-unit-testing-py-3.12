# Implementing, Testing, & Timing Sorting Algorithms Using Python's 3.12 New Features

[![python][0]][1]
[![license MIT][6]][7]
[![style black][8]][9]
[![lint: flake8][2]][3]
[![test: unittest][4]][5]

This project is a quick review of:
  * Python's 3.12 new features
  * Python's native unit testing module `unittest`
  * Python's type hint system
  * Measuring the running time of a function
  * Six basic sorting algorithms

This project also serves as the notes of said review. You'll find some theory in the
comments, docstrings, and readme.

The six basic sorting algorithms reviewed:
  * Selection Sort
  * Bubble Sort
  * Insertion Sort
  * Merge Sort
  * Heap Sort
  * Quick Sort

Only one version of each algorithm is chosen and implemented.

## Installation

Installation is required to run this program. Once you clone this repository,
install the dependencies with:

```bash
python -m pip install -r requirements.txt
```

## How to Run

The main functionality of the program is to measure and compare the running time of
different sorting algorithms. To run using default values use:

```bash
python main.py
```

If you want to provide your own values, the program accepts two command line
arguments: the size of the list to be sorted, and the number of times that the
measurement will be repeated and accumulated:

```bash
python main.py 20 50
```

The above will sort arrays of size 20, 50 different times, and the results added
together.

### Static Type Check

Note that `mypy` might not yet support type aliases, but `pyright` already does.

```bash
python -m pyright .
python -m mypy .
```

### Linting & Formatting

```bash
python -m black .
python -m flake8 .
```

### Unit Testing

This project uses the `unittest` native Python module to write and run unit testing.

To run tests use either:

```bash
python sort_test.py
python -m unittest sort_test.py
```

## Analysis of Used Implementations

| algorithm      | time complexity (best avg worst) | space complexity (total aux) |
| ---:           | :---:                            | :---:                        |
| selection sort | O(n^2) O(n^2) O(n^2)             | O(n) O(1)                    |
| bubble sort    | O(n) O(n^2) O(n^2)               | O(n) O(1)                    |
| insertion sort | O(n) O(n^2) O(n^2)               | O(n) O(1)                    |
| merge sort     | O(n log n) O(n log n) O(n log n) | O(n) O(n)                    |
| heap sort      | O(n log n) O(n log n) O(n log n) | O(n) O(1)                    |
| quick sort     | O(n log n) O(n log n) O(n^2)     | O(n) O(n)                    |

## Contributing

Found a bug, typo, or mistake? Want to refactor, optimize, or improve something in this
repository? **Send a pull request! Pull requests are always welcome!**

There's no need to create an issue. Just use a descriptive commit message and I'll
format it adequately when accepting the pull request. Contributing here is as simple
as commiting your changes and sending a pull request!

## Resources

### Python

  * https://en.wikipedia.org/wiki/History_of_Python

### What's New in Python 3.12

  * https://docs.python.org/3/whatsnew/3.12.html
  * https://realpython.com/python312-new-features/
  * https://blog.jetbrains.com/pycharm/2023/11/python-3-12/

### Algorithms & Data Structures

  * https://www.bigocheatsheet.com/
  * https://rosettacode.org/wiki/Sorting
  * https://rosettacode.org/wiki/Category:Sorting_Algorithms

### Selection Sort

  * https://en.wikipedia.org/wiki/selection_sort
  * https://rosettacode.org/wiki/Sorting_algorithms/Selection_sort
  * https://www.programiz.com/dsa/selection-sort

### Bubble Sort

  * https://en.wikipedia.org/wiki/bubble_sort
  * https://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort
  * https://www.programiz.com/dsa/bubble-sort

### Insertion Sort

  * https://en.wikipedia.org/wiki/insertion_sort
  * https://rosettacode.org/wiki/Sorting_algorithms/Insertion_sort
  * https://www.programiz.com/dsa/insertion-sort

### Merge Sort

  * https://en.wikipedia.org/wiki/merge_sort
  * https://rosettacode.org/wiki/Sorting_algorithms/Merge_sort
  * https://www.programiz.com/dsa/merge-sort

### Heap Sort

  * https://en.wikipedia.org/wiki/heap_sort
  * https://rosettacode.org/wiki/Sorting_algorithms/Heapsort
  * https://www.programiz.com/dsa/heap-sort

### Quick Sort

  * https://en.wikipedia.org/wiki/quick_sort
  * https://rosettacode.org/wiki/Sorting_algorithms/Quicksort
  * https://www.programiz.com/dsa/quick-sort

---

[0]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[1]: https://github.com/python/cpython
[2]: https://img.shields.io/badge/lint-flake8-blue.svg
[3]: https://github.com/PyCQA/flake8
[4]: https://img.shields.io/badge/test-unittest-blue.svg
[5]: https://docs.python.org/3/library/unittest.html
[6]: https://badgen.net/github/license/JCPedroza/algorithms-and-data-structures-py
[7]: https://opensource.org/licenses/MIT
[8]: https://img.shields.io/badge/code%20style-black-000000.svg
[9]: https://github.com/psf/black
