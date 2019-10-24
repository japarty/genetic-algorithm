import random
import math

def population(individuals_value,chromosomes_value):
    population=[]
    for i in range(individuals_value):
        population.append([])
        for q in range(chromosomes_value):
            population[i].append(random.randint(65,90))
    return population

def ocena_przystosowania(population):
    test=[ord('K'),ord('O'),ord('G'),ord('N'),ord('I'),ord('T'),ord('Y'),ord('W'),ord('I'),ord('S'),ord('T'),ord('Y'),ord('K'),ord('A')]
    różnice=[0]*len(population)
    for i in range(len(population)):
        for q in range(len(population[i])):
            różnice[i]+=int(math.fabs(test[q]-population[i][q]))
    return min(różnice)

def suma_przystosowania(population):
    test=[ord('K'),ord('O'),ord('G'),ord('N'),ord('I'),ord('T'),ord('Y'),ord('W'),ord('I'),ord('S'),ord('T'),ord('Y'),ord('K'),ord('A')]
    różnice=[0]*len(population)
    for i in range(len(population)):
        for q in range(len(population[i])):
            różnice[i]+=int(math.fabs(test[q]-population[i][q]))
    return sum(różnice)

def ruletka(population):
    suma_różnic=suma_przystosowania(population)
    kolo=[]
    for i in range(len(population)):
        if i==0: poprzednia=0
        else: poprzednia=kolo[i-1]
        kolo.append(poprzednia+(ocena_przystosowania([population[i]])/suma_różnic))
    nowa_populacja=[]
    for i in population:
        loteria=random.uniform(0, 1)
        for q in range(len(kolo)):
            if loteria<=kolo[q]:
                nowa_populacja.append(population[q])
                break
    return nowa_populacja

def crossing(population,crossing_chance):
    for i in range(0,len(population),2): #problem z nieparzystymi?
        if random.uniform(0, 1)<=crossing_chance:
            miejsce_ciecia=random.randint(1,len(population[i])-1)
            print(i,miejsce_ciecia)
            temp_1=population[i][:miejsce_ciecia]
            temp_2=population[i+1][miejsce_ciecia:]
            population[i]=population[i][:miejsce_ciecia]+temp_2
            population[i+1]=temp_1+population[i+1][miejsce_ciecia:]
    return population


population=population(8,14)
print(population)
'''
while ocena_przystosowania(population)>0:
    population=ruletka(population)
    population=crossing(population,0.8)
'''
population=ruletka(population)
print(population)
population=crossing(population,0.8)
print(population)
