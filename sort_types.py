from dataclasses import dataclass
from typing import Callable

type Seconds = float
type IntList = list[int]
type Sorter = Callable[[IntList], IntList]


@dataclass(frozen=True)
class Algorithm:
    sort: Sorter
    name: str


type AlgorithmList = list[Algorithm]
