import abc

import numpy as np

from genetic_algorithms.src.base_classes.individual import Individual


class Mutation(abc.ABC):
    """
    The base class for mutation strategies
    """

    def __call__(self, population: list[Individual]) -> list[Individual]:
        for individual in population:
            individual.chromosome = self.mutate_chromosome(individual.chromosome)

        return population

    @abc.abstractmethod
    def mutate_chromosome(self, chromosome: np.ndarray) -> np.ndarray:
        pass
