import string

import numpy as np

from genetic_algorithms.src.base_classes.fitness_calculator import FitnessCalculator
from genetic_algorithms.src.base_classes.individual import Individual
from genetic_algorithms.src.crossovers.uniform_crossover import UniformCrossover
from genetic_algorithms.src.mutations.random_resetting_mutation import RandomResettingMutation
from genetic_algorithms.src.selections.elitist_fraction_selection import ElitistFractionSelection
from genetic_algorithms.src.simulation import Simulation
from genetic_algorithms.src.simulation_loggers.string_printer import StringPrinter
from genetic_algorithms.src.utilities.random import select_random_items, set_random_seed


def initialize_individual(sequence_length: int, possible_characters: list[str]):
    characters = select_random_items(possible_characters, sequence_length)
    return Individual(np.array(characters))


class SequenceMatcher(FitnessCalculator):
    def __init__(self, target_string: str):
        self.target_string = target_string

    def calculate_fitness(self, sequence: Individual) -> float:
        score = 0

        for c1, c2 in zip(sequence.chromosome, self.target_string):
            if c1 == c2:
                score += 1

        return score


def main():
    set_random_seed(1)

    population_size = 1000
    n_generations = 1000
    possible_characters = list(string.ascii_letters + string.digits + string.punctuation + ' ')
    target_string = "This is an example of string generation from noise using genetic algorithms."

    initial_population = [initialize_individual(len(target_string), possible_characters)
                          for _ in range(population_size)]

    simulation = Simulation(
        population_size=population_size,
        number_of_generations=n_generations,
        initial_population=initial_population,
        fitness_calculator=SequenceMatcher(target_string),
        target_fitness=len(target_string),
        selection=ElitistFractionSelection(0.1),
        crossover=UniformCrossover(),
        mutation=RandomResettingMutation(0.1, possible_characters),
        logger=StringPrinter()
    )

    simulation.run()


if __name__ == "__main__":
    main()
