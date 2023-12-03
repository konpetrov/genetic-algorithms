import abc

from genetic_algorithms.src.base_classes.individual import Individual
from genetic_algorithms.src.utilities.random import select_non_repeating_random_items


class Crossover(abc.ABC):
    """
    The base class for crossover strategies.

    The number of parents is usually 2, but since multi-parent variations exists,
    the implementation should explicitly implement the ``get_number_of_parents`` method
    for the correct computations to take place.

    TODO: discuss the possibility of making the number of parents default to 2 without the need to define it explicitly.
    """

    def __call__(self,
                 breeding_population: list[Individual],
                 target_number_of_offsprings: int) -> list[Individual]:
        offsprings = []

        while len(offsprings) < target_number_of_offsprings:
            parents = select_non_repeating_random_items(breeding_population, self.get_number_of_parents())
            children = self.generate_offsprings(parents)

            for child in children:
                offsprings.append(child)

        return offsprings[:target_number_of_offsprings]

    @abc.abstractmethod
    def get_number_of_parents(self) -> int:
        pass

    @abc.abstractmethod
    def generate_offsprings(self, parents: list[Individual]) -> list[Individual]:
        pass
