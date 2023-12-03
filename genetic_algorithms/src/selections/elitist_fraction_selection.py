from genetic_algorithms.src.base_classes.individual import Individual
from genetic_algorithms.src.base_classes.selection import Selection


class ElitistFractionSelection(Selection):
    """
    Selects a percentage of fittest individuals for breeding
    """

    def __init__(self, fraction: float):
        self.fraction = fraction

    def __call__(self, population: list[Individual]) -> list[Individual]:
        sorted_individuals = sorted(population, key=lambda i: -i.fitness)
        number_to_select = round(self.fraction * len(population))
        return sorted_individuals[:number_to_select]
