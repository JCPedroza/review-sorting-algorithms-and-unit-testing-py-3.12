from dataclasses import dataclass
from typing import Callable

type FloatSeconds = float
type IntList = list[int]
type Sorter = Callable[[IntList], IntList]


@dataclass(frozen=True)
class SortingAlgorithm:
    sort: Sorter
    name: str


type SortingAlgorithmList = list[SortingAlgorithm]
