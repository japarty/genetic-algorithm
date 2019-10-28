import random
import math

test = [ord('K'),ord('O'),ord('G'),ord('N'),ord('I'),ord('T'),ord('Y'),ord('W'),ord('I'),ord('S'),ord('T'),ord('Y'),ord('K'),ord('A')]
HOW_MANY_CHROMOSOMES = 20
HOW_MANY_GENES = len(test)
CROSSING_CHANCE = 0.8
MUTATION_CHANCE = 0.02

def generate_population(individuals_value,chromosomes_value):
    population = []
    for i in range(individuals_value):
        population.append([])
        for q in range(chromosomes_value):
            population[i].append(random.randint(ord('A'),ord('Z')))
    return population

def fitness_evaluation(population,test):
    differences = [0]*len(population)
    for i in range(len(population)):
        for q in range(len(population[i])):
            differences[i]+=int(math.fabs(test[q]-population[i][q]))
    return differences

def roulette(population): #not working
    sum_of_differences = sum(fitness_evaluation(population,test))
    wheel = []
    for i in range(len(population)):
        if i==0: last_value = 0
        else: last_value=wheel[i-1]
        wheel.append(last_value+(min(fitness_evaluation([population[i]],test))/sum_of_differences))
    new_population=[]
    for i in population:
        lottery = random.uniform(0, 1)
        for q in range(len(wheel)):
            if lottery<=wheel[q]:
                new_population.append(population[q])
                break
    return new_population

def ranking(population):
    tournament = []
    for individual in population:
        tournament.append([population[random.randint(0,len(population)-1)],population[random.randint(0,len(population)-1)]])
    new_population=[]
    for battle in tournament:
        fighter_a = fitness_evaluation([battle[0]],test)
        fighter_b = fitness_evaluation([battle[1]],test)
        if fighter_a<fighter_b: new_population.append(battle[0])
        elif fighter_a>fighter_b: new_population.append(battle[1])
        elif fighter_a==fighter_b: new_population.append(battle[random.randint(0,1)])
    return new_population

def crossing(population,CROSSING_CHANCE):
    for i in range(0,len(population),2): #problem z nieparzystymi?
        if random.uniform(0, 1)<=CROSSING_CHANCE:
            cut_place = random.randint(1,len(population[i])-1)
            temp_1=population[i][cut_place:]
            temp_2=population[i+1][cut_place:]
            population[i] = population[i][:cut_place]+temp_2
            population[i+1] = population[i+1][:cut_place]+temp_1
    return population

def mutation(population,MUTATION_CHANCE):
    for individual in population:
        if random.uniform(0,1)<=MUTATION_CHANCE:
            mutating_genome=random.randint(0,len(individual)-1)
            individual[mutating_genome] = random.randint(ord('A'),ord('Z'))
    return population

def gen_alg(HOW_MANY_CHROMOSOMES,HOW_MANY_GENES,CROSSING_CHANCE,MUTATION_CHANCE):
    population = generate_population(HOW_MANY_CHROMOSOMES,HOW_MANY_GENES)
    print(population)
    loops = 0
    while min(fitness_evaluation(population,test))>0:
        loops+=1
        if loops%100==0: print('i=',loops,min(fitness_evaluation(population,test)))
        population = roulette(population)
        population = crossing(population,CROSSING_CHANCE)
        population = mutation(population,MUTATION_CHANCE)
    print(loops)
    print(population)
    if test in population:
        print(test)
        print(population[population.index(test)])

gen_alg(HOW_MANY_CHROMOSOMES,HOW_MANY_GENES,CROSSING_CHANCE,MUTATION_CHANCE)
