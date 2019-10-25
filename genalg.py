import random
import math

test=[ord('K'),ord('O'),ord('G'),ord('N'),ord('I'),ord('T'),ord('Y'),ord('W'),ord('I'),ord('S'),ord('T'),ord('Y'),ord('K'),ord('A')]
HOW_MANY_CHROMOSOMES=20
HOW_MANY_GENES=len(test)
CROSSING_CHANCE=0.8
MUTATION_CHANCE=0.02

def population(individuals_value,chromosomes_value):
    population=[]
    for i in range(individuals_value):
        population.append([])
        for q in range(chromosomes_value):
            population[i].append(random.randint(ord('A'),ord('Z')))
    return population

def fitness_evaluation(population,test):
    differences=[0]*len(population)
    for i in range(len(population)):
        for q in range(len(population[i])):
            differences[i]+=int(math.fabs(test[q]-population[i][q]))
    return min(differences)

def fitness_sum(population,test):
    differences=[0]*len(population)
    for i in range(len(population)):
        for q in range(len(population[i])):
            differences[i]+=int(math.fabs(test[q]-population[i][q]))
    return sum(differences)

def roulette(population): #not working
    suma_różnic=fitness_sum(population,test)
    kolo=[]
    for i in range(len(population)):
        if i==0: poprzednia=0
        else: poprzednia=kolo[i-1]
        kolo.append(poprzednia+(fitness_evaluation([population[i]],test)/suma_różnic))
    nowa_populacja=[]
    for i in population:
        loteria=random.uniform(0, 1)
        for q in range(len(kolo)):
            if loteria<=kolo[q]:
                nowa_populacja.append(population[q])
                break
    return nowa_populacja

def ranking(population):
    tournament=[]
    for individual in population:
        tournament.append([population[random.randint(0,len(population)-1)],population[random.randint(0,len(population)-1)]])
    new_population=[]
    for battle in tournament:
        if fitness_evaluation([battle[0]],test)<fitness_evaluation([battle[1]],test):
            new_population.append(battle[0])
        elif fitness_evaluation([battle[0]],test)>fitness_evaluation([battle[1]],test):
            new_population.append(battle[1])
        elif fitness_evaluation([battle[0]],test)==fitness_evaluation([battle[1]],test):
            new_population.append(battle[random.randint(0,1)])
    return new_population

def crossing(population,CROSSING_CHANCE):
    for i in range(0,len(population),2): #problem z nieparzystymi?
        if random.uniform(0, 1)<=CROSSING_CHANCE:
            miejsce_ciecia=random.randint(1,len(population[i])-1)
            temp_1=population[i][miejsce_ciecia:]
            temp_2=population[i+1][miejsce_ciecia:]
            population[i]=population[i][:miejsce_ciecia]+temp_2
            population[i+1]=population[i+1][:miejsce_ciecia]+temp_1
    return population

def mutation(population,MUTATION_CHANCE):
    for individual in population:
        if random.uniform(0,1)<=MUTATION_CHANCE:
            mutating_genome=random.randint(0,len(individual)-1)
            individual[mutating_genome]=random.randint(ord('A'),ord('Z'))
    return population


population=population(HOW_MANY_CHROMOSOMES,HOW_MANY_GENES)
print(population)
loops=0

while fitness_evaluation(population,test)>0:
    loops+=1
    if loops%100==0: print('i=',loops,fitness_evaluation(population,test))
    population=ranking(population)
    population=crossing(population,CROSSING_CHANCE)
    population=mutation(population,MUTATION_CHANCE)
print(loops)
print(population)
