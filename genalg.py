import random
import math
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier as KNC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score



'''data load'''
data = pd.read_csv('features_train.csv')
target = data['target']
data = data.drop("target", axis=1)

test = pd.read_csv('features_test.csv')
test_target = test['target']
test = test.drop("target", axis=1)


ile=0
for q in data:
    ile+=1

HOW_MANY_CHROMOSOMES = 20
HOW_MANY_GENES = ile
CROSSING_CHANCE = 0.8
MUTATION_CHANCE = 0.05

def generate_population(individuals_value,chromosomes_value):
    population = []
    for i in range(individuals_value):
        population.append([])
        for q in range(chromosomes_value):
            population[i].append(random.randint(0,1))
    return population

def fitness_evaluation(population,data,target,test,test_target):
    fitness = [0]*len(population)
    for i in range(len(population)):
        ind_data=pd.DataFrame()
        ind_test=pd.DataFrame()
        n=0
        for q in data:
            if population[i][n]==1:
                ind_data[q] = pd.Series(data[q])
                ind_test[q] = pd.Series(test[q])
            n+=1
        clf = LDA()
        clf.fit(ind_data, target)
        LDA()
        new=clf.predict(ind_test)
        fitness[i]=accuracy_score(new,test_target)
    return fitness

def ranking(population,fitness):
    tournament = []
    fitness_tournament = []
    for individual in population:
        a = random.randint(0,len(population)-1)
        b = random.randint(0,len(population)-1)
        tournament.append([population[a],population[b]])
        fitness_tournament.append([fitness[a],fitness[b]])
    new_population=[]
    for battle in range(len(tournament)):
        fighter_a = fitness_tournament[battle][0]
        fighter_b = fitness_tournament[battle][0]
        if fighter_a<fighter_b: new_population.append(tournament[battle][0])
        elif fighter_a>fighter_b: new_population.append(tournament[battle][1])
        elif fighter_a==fighter_b: new_population.append(tournament[battle][random.randint(0,1)])
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
            individual[mutating_genome] = random.randint(0,1)
    return population

def gen_alg(HOW_MANY_CHROMOSOMES,HOW_MANY_GENES,CROSSING_CHANCE,MUTATION_CHANCE):
    population = generate_population(HOW_MANY_CHROMOSOMES,HOW_MANY_GENES)
    print(population)
    fitness = fitness_evaluation(population,data,target,test,test_target)
    loops = 0
    while min(fitness)<100 and loops<100:
        loops+=1
        population = ranking(population,fitness)
        population = crossing(population,CROSSING_CHANCE)
        population = mutation(population,MUTATION_CHANCE)
        fitness = fitness_evaluation(population,data,target,test,test_target)
        len_pop = [sum(i) for i in population]
        print(loops,": ",max(fitness),len_pop,sum(population[fitness.index(max(fitness))]))
    return population,fitness

populacja,jakifitnes=gen_alg(HOW_MANY_CHROMOSOMES,HOW_MANY_GENES,CROSSING_CHANCE,MUTATION_CHANCE)
print(populacja)
print(jakifitnes)
