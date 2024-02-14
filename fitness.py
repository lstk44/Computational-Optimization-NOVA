from individual import Individual
from population import Population
from data import nutrients, commodities
from selection import roulette, ranked, tournament
from variation import crossover, mutation
from copy import deepcopy
import numpy as np 


def get_fitness(self):
    """This function calculates the fitness value of the corresponding individual by summing up the prices of included items. 
    For every broken constraint, the fitness will be penalized. The function returns, the fitness, the total costs/price and total nutritions of the individual
    
    Returns:
        int: fitness 
        int: total cost/price
        list: total nutrion values of that individual
    """
    # Create vector of total costs and total nutrional values of the individual
    commodities_matrix = np.array(list(commodities.values()))
    commodities_of_individual = self.representation.dot(commodities_matrix)
    
    # Create constraints list and check which constraints are fulfilled/broken
    constraints = np.array(list(nutrients.values()))
    check = constraints <= commodities_of_individual[1:] # min constraints

    # Initial fitness based on costs
    fitness = commodities_of_individual[0]
    costs = fitness

    # Increase fitness for every broken constraint
    for i in range(len(constraints)):
        if check[i] == False:
            fitness += 10 

    return fitness, costs, commodities_of_individual[1:]