import random
import math
import numpy as np

aim = [ord('K'),ord('O'),ord('G'),ord('N'),ord('I'),ord('T'),ord('Y'),ord('W'),ord('I'),ord('S'),ord('T'),ord('Y'),ord('K'),ord('A')]
HOW_MANY_CHROMOSOMES = 20
HOW_MANY_GENES = len(aim)
CROSSOVER_PROBABILITY = 0.8
MUTATION_PROBABILITY = 0.02

def fitness_evaluation(population,aim):
    differences = np.zeros(population.shape[0])
    for i in range(population.shape[0]):
        for q in range(len(population[i])):
            differences[i]+=int(math.fabs(aim[q]-population[i][q]))
    return differences

def roulette_wheel_selection(population): #not working
    sum_of_differences = sum(fitness_evaluation(population,aim))
    wheel = []
    for i in range(population.shape[0]):
        if i==0: last_value = 0
        else: last_value=wheel[i-1]
        wheel.append(last_value+(min(fitness_evaluation([population[i]],aim))/sum_of_differences))
    new_population=[]
    for i in population:
        lottery = random.uniform(0, 1)
        for q in range(len(wheel)):
            if lottery<=wheel[q]:
                new_population.append(population[q])
                break
    return new_population

def ranking_selection(population):
    tournament = []
    for individual in population:
        tournament.append([population[random.randint(0,population.shape[0]-1)],population[random.randint(0,population.shape[0]-1)]])
    new_population=[]
    for battle in tournament:
        fighter_a = fitness_evaluation(battle[0],aim)
        fighter_b = fitness_evaluation(battle[1],aim)
        if fighter_a<fighter_b: new_population.append(battle[0])
        elif fighter_a>fighter_b: new_population.append(battle[1])
        elif fighter_a==fighter_b: new_population.append(battle[random.randint(0,1)])
    return new_population

def crossing(population,CROSSOVER_PROBABILITY):
    for i in range(0,population.shape[0],2): #problem z nieparzystymi?
        if random.uniform(0, 1)<=CROSSOVER_PROBABILITY:
            cut_place = random.randint(1,len(population[i])-1)
            temp_1=population[i][cut_place:]
            temp_2=population[i+1][cut_place:]
            population[i] = population[i][:cut_place]+temp_2
            population[i+1] = population[i+1][:cut_place]+temp_1
    return population

def mutation(population,MUTATION_PROBABILITY):
    for individual in population:
        if random.uniform(0,1)<=MUTATION_PROBABILITY:
            mutating_genome=random.randint(0,len(individual)-1)
            individual[mutating_genome] = random.randint(ord('A'),ord('Z'))
    return population

def gen_alg(HOW_MANY_CHROMOSOMES,HOW_MANY_GENES,CROSSOVER_PROBABILITY,MUTATION_PROBABILITY):
    population = np.random.randint(ord('A'),ord('Z'),size=(HOW_MANY_CHROMOSOMES,HOW_MANY_GENES))
    print(population)
    loops = 0
    while min(fitness_evaluation(population,aim))>0:
        loops+=1
        if loops%100==0: print('i=',loops,min(fitness_evaluation(population,aim)))
        population = ranking_selection(population)
        population = crossing(population,CROSSOVER_PROBABILITY)
        population = mutation(population,MUTATION_PROBABILITY)
    print(loops)
    print(population)

gen_alg(HOW_MANY_CHROMOSOMES,HOW_MANY_GENES,CROSSOVER_PROBABILITY,MUTATION_PROBABILITY)
