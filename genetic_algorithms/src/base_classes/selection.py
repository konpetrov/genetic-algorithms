import abc

from genetic_algorithms.src.base_classes.individual import Individual


class Selection(abc.ABC):
    """
    The base class for selection strategies.
    """

    @abc.abstractmethod
    def __call__(self, population: list[Individual]) -> list[Individual]:
        pass
