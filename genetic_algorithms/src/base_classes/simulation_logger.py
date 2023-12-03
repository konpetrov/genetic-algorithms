import abc

from genetic_algorithms.src.base_classes.individual import Individual


class SimulationLogger(abc.ABC):
    """
    The base class for simulation progress logging strategies.
    """

    @abc.abstractmethod
    def log(self, generation_index: int, fittest_individual: Individual):
        pass
