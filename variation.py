from data import nutrients, commodities
import numpy as np
from random import randint, sample
from individual import Individual

def crossover(parent1, parent2, xo_type='one-point'):
    """The function gets two parents, applies a crossover algorithm and returns the offsprings.
    The function allows four different crossover types: uniform, one-point, five-point and ten-point crossover.

    Args:
        parent1 (Individual): First individual for crossover.
        parent2 (Individual): Second individual for crossover.
        xo_type (str, optional): Crossover method that should be used. Defaults to "one-point".

    Returns:
        Individual: First offspring
        Individual: Second offspring
    """
    # Convert parents to lists
    parent1 = list(parent1)
    parent2 = list(parent2)

    # uniform crossover
    if xo_type == 'uniform':
        # Generate random choices for each element in the parents
        random_choices = np.random.randint(2, size=len(parent1))
        # Create offspring using uniform crossover
        offspring1 = np.where(random_choices, parent1, parent2)
        offspring2 = np.where(random_choices, parent2, parent1)
    # one-point crossover
    elif xo_type == 'one-point':
        # Select a random crossover point
        point = randint(1, len(parent1)-1)
        # Create offspring using one-point crossover
        offspring1 = parent1[:point] + parent2[point:]
        offspring2 = parent2[:point] + parent1[point:]
    # five-point crossover
    elif xo_type == 'five-point':
        # Select five random crossover points
        rl = np.array(sorted(sample(range(1, len(parent1)-1), 5)))
        # Create offspring using five-point crossover
        offspring1 = parent1[:rl[0]] + parent2[rl[0]:rl[1]] + parent1[rl[1]:rl[2]] + parent2[rl[2]:rl[3]] + parent1[rl[3]:rl[4]] + parent2[rl[4]:]
        offspring2 = parent2[:rl[0]] + parent1[rl[0]:rl[1]] + parent2[rl[1]:rl[2]] + parent1[rl[2]:rl[3]] + parent2[rl[3]:rl[4]] + parent1[rl[4]:]
    # ten-point crossover
    elif xo_type == 'ten-point':
        # Select ten random crossover points
        rl = np.array(sorted(sample(range(1, len(parent1)-1), 10)))
        # Create offspring using ten-point crossover
        offspring1 = parent1[:rl[0]] + parent2[rl[0]:rl[1]] + parent1[rl[1]:rl[2]] + parent2[rl[2]:rl[3]] + parent1[rl[3]:rl[4]] + parent2[rl[4]:rl[5]] + parent1[rl[5]:rl[6]] + parent2[rl[6]:rl[7]] + parent1[rl[7]:rl[8]] + parent2[rl[8]:rl[9]] + parent1[rl[9]:]
        offspring2 = parent2[:rl[0]] + parent1[rl[0]:rl[1]] + parent2[rl[1]:rl[2]] + parent1[rl[2]:rl[3]] + parent2[rl[3]:rl[4]] + parent1[rl[4]:rl[5]] + parent2[rl[5]:rl[6]] + parent1[rl[6]:rl[7]] + parent2[rl[7]:rl[8]] + parent1[rl[8]:rl[9]] + parent2[rl[9]:]

    # Return the resulting offspring
    return offspring1, offspring2


def mutation(
        individual,
        mutation_type="single_bit_flip",
        bit_flips=None, 
    ):
    """The function gets one individual, applies a mutation algorithm and returns the mutated individual.
    The function allows five different mutation types: single bit flip, complete bit flip, single swap mutation, multiple bit flip and scramble mutation.

    Args:
        individual (Individual): Individual for mutation.
        mutation_type (str, optional): Mutation method that should be used. Defaults to "single_bit_flip".
        bit_flips (int, optional): Number of bit flips if mutation_type="multiple_bit_flip_mutation". Defaults to None.

    Returns:
        Individual: Mutated individual
    """

    # Single Bit Flip Mutation
    if mutation_type == "single_bit_flip":
        # randomly select index of the bit to be flipped
        mutation_point = np.random.randint(len(individual), size=1)[0]
        # flip the bit
        if individual[mutation_point] == 1:
            individual[mutation_point] = 0
        elif individual[mutation_point] == 0:
            individual[mutation_point] = 1
        return individual

    # Complete Bit Flip Mutation
    # Flips all bits in the individual
    elif mutation_type == "complete_bit_flip":
        for i in range(len(individual)):
            if individual[i] == 1:
                individual[i] = 0
            elif individual[i] == 0:
                individual[i] = 1
        return individual

    # Swap Mutation (Single Bit)
    elif mutation_type == "single_swap_mutation":
        # get two indices of bits to be swaped
        mut_index = sample(range(len(individual)), 2)
        # swap bits
        individual[mut_index[0]], individual[mut_index[1]] = individual[mut_index[1]], individual[mut_index[0]]
        return individual

    # Multiple Bit Flip Mutation
    # Flips a specified number of bits in the individual
    # The number of bit flips is determined by the 'bit_flips' parameter
    elif mutation_type == "multiple_bit_flip_mutation":
        for _ in range(0,bit_flips):
            # randomly select index of the bit to be flipped
            mutation_point = np.random.randint(len(individual), size=1)[0]
            # flip bit
            if individual[mutation_point] == 1:
                individual[mutation_point] = 0
            elif individual[mutation_point] == 0:
                individual[mutation_point] = 1
        return individual

    # Scramble Mutation 
    elif mutation_type == "scramble_mutation":
        # randomly select indices that define the range of bits to be shuffled
        split_point_1 = np.random.randint(len(individual), size=1)[0]
        split_point_2 = np.random.randint(low=int(split_point_1), high=len(individual), size=1)[0]
        # shuffle bits in the specified range
        sublist = np.random.permutation(individual[split_point_1:split_point_2])
        individual[split_point_1:split_point_2] = sublist
        return individual