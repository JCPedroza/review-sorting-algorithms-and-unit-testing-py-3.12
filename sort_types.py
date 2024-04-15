from dataclasses import dataclass
from typing import Callable

type IntList = list[int]
type Sorter = Callable[[IntList], IntList]


@dataclass
class SortingAlgorithm:
    sort: Sorter
    name: str
