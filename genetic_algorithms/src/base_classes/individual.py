from __future__ import annotations

import numpy as np


class Individual:
    """
    A solution organism with a chromosome and a fitness score.
    The higher the fitness, the fitter the organism.
    """

    chromosome: np.ndarray
    fitness: float | None

    def __init__(self, chromosome: np.ndarray):
        self.chromosome = chromosome
        self.fitness = None
