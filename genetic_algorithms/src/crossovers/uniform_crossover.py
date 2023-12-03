import numpy as np

from genetic_algorithms.src.base_classes.crossover import Crossover
from genetic_algorithms.src.base_classes.individual import Individual
from genetic_algorithms.src.utilities.random import probability


class UniformCrossover(Crossover):
    """
    The crossover strategy,
    where each gene is inherited from either parent
    with the probability equal to ``swap_probability``.
    """

    swap_probability: float = 0.5

    def __init__(self, swap_probability: float = 0.5):
        self.swap_probability = swap_probability

    def get_number_of_parents(self) -> int:
        return 2

    def generate_offsprings(self, parents: list[Individual]) -> list[Individual]:
        offspring_1_chromosome = []
        offspring_2_chromosome = []

        parent_1, parent_2 = parents

        for gene_1, gene_2 in zip(parent_1.chromosome, parent_2.chromosome):
            if probability(self.swap_probability):
                offspring_1_chromosome.append(gene_2)
                offspring_2_chromosome.append(gene_1)
            else:
                offspring_1_chromosome.append(gene_1)
                offspring_2_chromosome.append(gene_2)

        offspring_1 = Individual(np.array(offspring_1_chromosome))
        offspring_2 = Individual(np.array(offspring_2_chromosome))

        return [offspring_1, offspring_2]
