from genetic_algorithms.src.base_classes.crossover import Crossover
from genetic_algorithms.src.base_classes.fitness_calculator import FitnessCalculator
from genetic_algorithms.src.base_classes.individual import Individual
from genetic_algorithms.src.base_classes.mutation import Mutation
from genetic_algorithms.src.base_classes.selection import Selection
from genetic_algorithms.src.base_classes.simulation_logger import SimulationLogger


class Simulation:
    population_size: int
    number_of_generations: int
    initial_population: list[Individual]
    fitness_calculator: FitnessCalculator
    target_fitness: float
    selection: Selection
    crossover: Crossover
    mutation: Mutation
    logger: SimulationLogger

    def __init__(self,
                 population_size: int,
                 number_of_generations: int,
                 initial_population: list[Individual],
                 fitness_calculator: FitnessCalculator,
                 target_fitness: float,
                 selection: Selection,
                 crossover: Crossover,
                 mutation: Mutation,
                 logger: SimulationLogger):
        self.population_size = population_size
        self.number_of_generations = number_of_generations
        self.initial_population = initial_population
        self.fitness_calculator = fitness_calculator
        self.target_fitness = target_fitness
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self.logger = logger

    def run(self):
        population = self.initial_population

        for generation_index in range(self.number_of_generations):
            self.fitness_calculator(population)

            fittest_individual = max(population, key=lambda individual: individual.fitness)

            if self.logger:
                self.logger.log(generation_index, fittest_individual)

            if fittest_individual.fitness >= self.target_fitness:
                break

            selected_population = self.selection(population)
            number_of_offsprings_to_produce = self.population_size - len(selected_population)
            offsprings = self.crossover(selected_population, number_of_offsprings_to_produce)
            mutated_offsprings = self.mutation(offsprings)
            population = [*selected_population, *mutated_offsprings]
