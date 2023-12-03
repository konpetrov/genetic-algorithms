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


class SentencePalindromeDetector(FitnessCalculator):
    def calculate_fitness(self, sequence: Individual) -> float:
        reversed_chromosome = sequence.chromosome.copy()[::-1]

        sentence_character_count = sum(c.isalpha() or c == ' ' for c in sequence.chromosome)
        palindrome_score = 0

        for c1, c2 in zip(sequence.chromosome, reversed_chromosome):
            if c1 == c2:
                palindrome_score += 1
            else:
                break

        is_sentence_probability = sentence_character_count / len(sequence.chromosome)
        is_palindrome_probability = palindrome_score / len(sequence.chromosome)

        return is_sentence_probability * is_palindrome_probability


def main():
    set_random_seed(1)

    population_size = 1000
    n_generations = 1000
    possible_characters = list(string.ascii_lowercase + string.digits + string.punctuation + ' ')
    length = 80

    initial_population = [initialize_individual(length, possible_characters)
                          for _ in range(population_size)]

    fitness_calculator = SentencePalindromeDetector()

    simulation = Simulation(
        population_size=population_size,
        number_of_generations=n_generations,
        initial_population=initial_population,
        fitness_calculator=fitness_calculator,
        target_fitness=1,
        selection=ElitistFractionSelection(0.1),
        crossover=UniformCrossover(),
        mutation=RandomResettingMutation(0.01, possible_characters),
        logger=StringPrinter()
    )

    simulation.run()


if __name__ == "__main__":
    main()
