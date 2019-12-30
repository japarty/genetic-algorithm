import random
import math
import numpy as np

aim = [ord('K'),ord('O'),ord('G'),ord('N'),ord('I'),ord('T'),ord('Y'),ord('W'),ord('I'),ord('S'),ord('T'),ord('Y'),ord('K'),ord('A')]
HOW_MANY_CHROMOSOMES = 20
HOW_MANY_GENES = len(aim)
CROSSOVER_PROBABILITY = 0.8
MUTATION_PROBABILITY = 0.02

def generate_population(individuals_value,chromosomes_value):
    population = []
    for i in range(individuals_value):
        population.append([])
        for q in range(chromosomes_value):
            population[i].append(random.randint(ord('A'),ord('Z')))
    return population

    def gen_fast(individuals_value,chromosomes_value):
        population = [[random.randint(ord('A'),ord('Z')) for i in range(chromosomes_value)] for q in range(individuals_value)]
        return population

a=np.random.randint(ord('A'),ord('Z'),size=(HOW_MANY_CHROMOSOMES,HOW_MANY_GENES))
print(a[0][1])
