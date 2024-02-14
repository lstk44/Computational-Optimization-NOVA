from data import nutrients, commodities
import numpy as np
from random import choice
from operator import attrgetter


def roulette(pop):
    """This function performs a fitness proportinate selection (roulette selection) and returns the selected individual of the population.

    Args:
        pop (Population): Current population object.

    Returns:
        Individual: Selected individual 
    """
    # Extract the fitness values for each individual in the population
    fitness = [individual.fitness for individual in pop]
    
    # Calculate the sum of fitness values in the population
    sum_fitness_in_pop = sum(fitness)
    
    # Invert the fitness values by subtracting them from the sum of fitness in the population
    inverted_fitness = sum_fitness_in_pop - np.array(fitness)
    
    # Calculate the selection probabilities based on the inverted fitness values
    probability = inverted_fitness / sum(inverted_fitness)
    
    # Create a range of indices corresponding to the population
    pop_range = np.arange(len(pop))
    
    # Randomly select an index from the range using the selection probabilities
    select = np.random.choice(pop_range, p=probability)
    
    # Retrieve the individual from the population based on the selected index
    individual = pop[select]
    
    # Return the selected individual
    return individual


def ranked(pop):
    """This function performs a ranking selection and returns the selected individual of the population.

    Args:
        pop (Population): Current population object.

    Returns:
        Individual: Selected individual 
    """
    # Sort the population based on individual fitness in descending order
    sorted_pop = sorted(pop, key=lambda individual: individual.fitness, reverse=True)
    
    # Calculate the denominator for creating a probability distribution
    denominator = sum(list(range(len(sorted_pop)+1)))
    
    # Create a probability distribution based on the rank of each individual
    dist = [i/denominator for i in list(range(1,len(sorted_pop)+1))]
    
    # Randomly select an index from the population using the probability distribution
    index = np.random.choice(list(range(len(sorted_pop))), p=dist)
    
    # Return the selected individual from the population
    return sorted_pop[index]


def tournament(pop,k):
    """This function performs a tournament selection and returns the selected individual of the population.

    Args:
        pop (Population): Current population object.
        k (int): Size of the tournament. 

    Returns:
        Individual: Selected individual 
    """
    tournament = []
    for _ in range(k):
        # Randomly select an individual from the population and add it to the tournament
        tournament.append(choice(pop))
    
    # Return the individual with the minimum fitness value in the tournament
    return min(tournament, key=attrgetter("fitness"))
