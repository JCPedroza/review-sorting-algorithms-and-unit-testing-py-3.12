# Implementing & Testing Sorting Algorithms Using Python 3.12 New Features

This project is a quick review of:
  * Python 3.12 new features
  * Python native unit testing module `unittest`
  * Sorting algorithms

This project also serves as the notes of said review. Expect to see some theory in the
comments, docstrings, and readme.

## Installation

Installation is only needed for static type check and formatting. Note that
`mypy` might not yet support type aliases, but `pyright` already does.

```bash
python -m pip install -r requirements.txt
```

## Unit Testing

This project uses the `unittest` native Python module to write and run unit testing.

To run tests use either:

```bash
python sort_test.py
python -m unittest sort_test.py
```

## Analysis of Used Implementations

| algorithm      | time complexity (best avg worst)| space complexity (total aux)|
| ---            | ---                             | ---                         |
| selection sort | O(n^2) O(n^2) O(n^2)            | O(n) O(1)                   |
| bubble sort    | O(n) O(n^2) O(n^2)              | O(n) O(1)                   |
| insertion sort | O(n) O(n^2) O(n^2)              | O(n) O(1)                   |

## Resources

  * https://en.wikipedia.org/wiki/selection_sort
  * https://www.programiz.com/dsa/selection-sort
  * https://rosettacode.org/wiki/Sorting_algorithms/Selection_sort

  * https://en.wikipedia.org/wiki/bubble_sort
  * https://www.programiz.com/dsa/bubble-sort
  * https://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort

  * https://en.wikipedia.org/wiki/insertion_sort
  * https://www.programiz.com/dsa/insertion-sort
  * https://rosettacode.org/wiki/Sorting_algorithms/Insertion_sort
