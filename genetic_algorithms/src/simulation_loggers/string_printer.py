from genetic_algorithms.src.base_classes.individual import Individual
from genetic_algorithms.src.base_classes.simulation_logger import SimulationLogger


class StringPrinter(SimulationLogger):
    def log(self, generation_index: int, fittest_individual: Individual):
        formatted_string = ''.join(fittest_individual.chromosome.tolist())
        print(f'{generation_index + 1}\t{formatted_string}')
