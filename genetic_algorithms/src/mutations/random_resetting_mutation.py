import numpy as np

from genetic_algorithms.src.base_classes.mutation import Mutation
from genetic_algorithms.src.utilities.random import probability, select_random_item


class RandomResettingMutation(Mutation):
    def __init__(self, gene_mutation_probability: float, gene_pool: list):
        self.gene_mutation_probability = gene_mutation_probability
        self.gene_pool = gene_pool

    def mutate_chromosome(self, chromosome: np.ndarray) -> np.ndarray:
        mutated_chromosome = []

        for gene in chromosome:
            if probability(self.gene_mutation_probability):
                mutated_chromosome.append(select_random_item(self.gene_pool))
            else:
                mutated_chromosome.append(gene)

        return np.array(mutated_chromosome)
