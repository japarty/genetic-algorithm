import random
import math

test=[1,1,1,1,1,1,1,1]
HOW_MANY_CHROMOSOMES=20
HOW_MANY_GENES=len(test)
CROSSING_CHANCE=0.5
MUTATION_CHANCE=0.2

def population(individuals_value,chromosomes_value):
    population=[]
    for i in range(individuals_value):
        population.append([])
        for q in range(chromosomes_value):
            population[i].append(random.randint(0,1))
    return population

def ocena_przystosowania(population,test):
    różnice=[0]*len(population)
    for i in range(len(population)):
        for q in range(len(population[i])):
            różnice[i]+=int(math.fabs(test[q]-population[i][q]))
    return min(różnice)

def suma_przystosowania(population,test):
    różnice=[0]*len(population)
    for i in range(len(population)):
        for q in range(len(population[i])):
            różnice[i]+=int(math.fabs(test[q]-population[i][q]))
    return sum(różnice)

def ruletka(population):
    suma_różnic=suma_przystosowania(population,test)
    kolo=[]
    for i in range(len(population)):
        if i==0: poprzednia=0
        else: poprzednia=kolo[i-1]
        kolo.append(poprzednia+(ocena_przystosowania([population[i]],test)/suma_różnic))
    nowa_populacja=[]
    for i in population:
        loteria=random.uniform(0, 1)
        for q in range(len(kolo)):
            if loteria<=kolo[q]:
                nowa_populacja.append(population[q])
                break
    return nowa_populacja

def crossing(population,CROSSING_CHANCE):
    for i in range(0,len(population),2): #problem z nieparzystymi?
        if random.uniform(0, 1)<=CROSSING_CHANCE:
            miejsce_ciecia=random.randint(1,len(population[i])-1)
            temp_1=population[i][:miejsce_ciecia]
            temp_2=population[i+1][miejsce_ciecia:]
            population[i]=population[i][:miejsce_ciecia]+temp_2
            population[i+1]=temp_1+population[i+1][miejsce_ciecia:]
    return population

def mutation(population,MUTATION_CHANCE):
    for individual in population:
        if random.uniform(0,1)<=MUTATION_CHANCE:
            mutating_genome=random.randint(0,len(individual)-1)
            individual[mutating_genome]=random.randint(0,1)
    return population


population=population(HOW_MANY_CHROMOSOMES,HOW_MANY_GENES)
print(population)
loops=0

while ocena_przystosowania(population,test)>0 and loops<=1000000:
    loops+=1
    if loops%100==0: print(ocena_przystosowania(population,test), loops)
    population=ruletka(population)
    population=crossing(population,CROSSING_CHANCE)
    population=mutation(population,MUTATION_CHANCE)
print(loops)
print(population)
'''
population=ruletka(population)
print(population)
population=crossing(population,0.8)
print(population)
population=mutation(population,0.8)
'''
