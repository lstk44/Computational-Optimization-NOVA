from data import commodities, nutrients
from random import random
from individual import Individual
from copy import deepcopy
from operator import attrgetter


class Population:
    def __init__(self, size, optim, **kwargs):
        self.individuals = []
        self.size = size
        self.optim = optim
        self.history_fitness = []
        self.history_calories = []
        self.history_protein = []
        self.history_carbohydrates = []
        self.history_fat = []
        self.history_sodium = []
        self.history_products = []
        for _ in range(size):
            self.individuals.append(
                Individual(
                size=kwargs["sol_size"],
                replacement=kwargs["replacement"],
                valid_set=kwargs["valid_set"],
            ))

    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]
    
    def __repr__(self):
        output = ""
        for individual in self.individuals:
            output = output + str(individual) + "\n"
        return output
    
    def evolve(self,
            select=None,
            tournament_k=None,
            crossover=None,
            mutate=None,
            gens= 100, 
            mut_prob = 0.2,
            mut_type = "single_bit_flip",
            bit_flips = None,
            xo_prob = 0.9,
            xo_type = "one-point",
            elitism=True
    ):
        """This function evolves the initial/current population over a defined number of generations. Through the parameters different methods
        for the selection, crossover and mutation can be assigned, as well as the crossover and mutation probabilites.  

        Args:
            select (function, optional): Pass a selection function (contains one selection algorithm). Defaults to None.
            tournament_k (int, optional): Tournament size if tournament selection is passed. Defaults to None.
            crossover (function, optional): Pass crossover function (can contain more crossover algorithms, the used one is specified in xo_type). Defaults to None.
            mutate (function, optional): Pass mutation function (can contain more mutation algorithms, the used one is specified in mut_type). Defaults to None.
            gens (int, optional): Number of generations. Defaults to 100.
            mut_prob (float, optional): Probability of mutating an offspring. Defaults to 0.2.
            mut_type (str, optional): Mutation method of the passed mutation function that should be used. Defaults to "single_bit_flip".
            bit_flips (int, optional): Number of bit flips if mut_type="multiple_bit_flip_mutation". Defaults to None.
            xo_prob (float, optional): Probability of applying crossover. Defaults to 0.9.
            xo_type (str, optional): Crossover method of the passed crossover function that should be used. Defaults to "one-point".
            elitism (bool, optional): Enable/Disable elitism. Defaults to True.
        """
        # Iterate over the specified number of generations
        for i in range(gens):
            new_gen = []
            
            # Generate a new generation
            while len(new_gen) < len(self):
                # Select parents for reproduction
                if tournament_k is None:
                    # Select two parents using the provided selection method
                    parent1, parent2 = select(self), select(self)
                else:
                    # Select two parents using tournament selection with k participants
                    parent1 = select(self, k=tournament_k)
                    parent2 = select(self, k=tournament_k)
                
                # Perform crossover to create offspring
                if random() < xo_prob:
                    # Perform crossover between parent1 and parent2 using the specified method
                    offspring1, offspring2 = crossover(parent1, parent2, xo_type)
                else: 
                    # Replicate parents if crossover probability is not met
                    offspring1 = parent1
                    offspring2 = parent2
                
                # Perform mutation on offsprings
                if random() < mut_prob: 
                    # Mutate offspring1 using the specified mutation method, bit flips, and cycles
                    offspring1 = mutate(offspring1, mut_type, bit_flips=bit_flips)
                if random() < mut_prob:
                    # Mutate offspring2 using the specified mutation method
                    offspring2 = mutate(offspring2, mut_type, bit_flips=bit_flips)
                
                # Add the offsprings to the new generation
                new_gen.append(Individual(offspring1))
                new_gen.append(Individual(offspring2))
            
            # Apply elitism by replacing the worst individuals in the current generation with the best individuals from the new generation
            if elitism:
                # elitism for maximization problem
                if self.optim == "max":
                    # Find the best individual in the current generation
                    elite = deepcopy(max(self.individuals, key=attrgetter("fitness")))
                    # Find the worst individual in the new generation
                    worst_new = min(new_gen, key=attrgetter("fitness"))
                    # Replace the worst individual with the elite individual if it has better fitness
                    if elite.fitness > worst_new.fitness:
                        new_gen.pop(new_gen.index(worst_new))
                        new_gen.append(elite)
                # elitism for minimization problem
                elif self.optim == "min":
                    # Find the best individual in the current generation
                    elite = deepcopy(min(self.individuals, key=attrgetter("fitness")))
                    # Find the worst individual in the new generation
                    worst_new = max(new_gen, key=attrgetter("fitness"))
                    # Replace the worst individual with the elite individual if it has better fitness
                    if elite.fitness < worst_new.fitness:
                        new_gen.pop(new_gen.index(worst_new))
                        new_gen.append(elite)
            
            # Update the current generation with the new generation
            self.individuals = new_gen
            
            # Store the fitness and other metrics of the best individual in each generation
            if self.optim == "max":
                best = max(self, key=attrgetter("fitness"))
            elif self.optim == "min":
                best = min(self, key=attrgetter("fitness"))
            self.history_fitness.append(best.fitness)
            self.history_calories.append(best.totals[0])
            self.history_fat.append(best.totals[1]) 
            self.history_sodium.append(best.totals[2]) 
            self.history_carbohydrates.append(best.totals[3]) 
            self.history_protein.append(best.totals[4]) 
        commodity_keys = list(commodities.keys())

        if self.optim == "max":
            for i, j in zip(max(self, key=attrgetter("fitness")).representation, commodity_keys):
                if i == 1:
                    self.history_products.append(j)
        elif self.optim == "min":
            for i, j in zip(min(self, key=attrgetter("fitness")).representation, commodity_keys):
                if i == 1:
                    self.history_products.append(j)