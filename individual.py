from random import sample
import numpy as np
from data import commodities, nutrients

class Individual:
    def __init__(
        self,
        representation=None,
        size=None,
        replacement=True,
        valid_set=None,
    ):
        if representation is None:
            if replacement == True:
                self.representation = np.array([np.random.choice(valid_set) for i in range(size)])
            elif replacement == False:
                self.representation = np.array(sample(valid_set, size))
        else:
            self.representation = np.array(representation)
        self.fitness, self.costs, self.totals = self.get_fitness()

    def get_fitness(self):
        raise Exception("You need to monkey patch the fitness path.")

    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value

    def __repr__(self):
        return f"Individual(size={len(self.representation)}); Fitness: {self.fitness}; Price: {self.costs}"

