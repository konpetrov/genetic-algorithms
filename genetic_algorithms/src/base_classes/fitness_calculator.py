import abc

from genetic_algorithms.src.base_classes.individual import Individual


class FitnessCalculator(abc.ABC):
    """
    The base class for fitness calculation strategies.

    The higher the fitness score, the fitter the chromosome.
    """

    def __call__(self, population: list[Individual]) -> list[Individual]:
        for individual in population:
            if individual.fitness is not None:
                continue

            individual.fitness = self.calculate_fitness(individual)

        return population

    @abc.abstractmethod
    def calculate_fitness(self, individual: Individual) -> float:
        pass
