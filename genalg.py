import random
import math
def populacja(ile_osobnikow,ile_chromosomow):
    populacja=[]
    for i in range(ile_osobnikow):
        populacja.append([])
        for q in range(ile_chromosomow):
            populacja[i].append(random.randint(65,90))
    return populacja

a=populacja(20,14)
'''
def ocena_przystosowania(populacja):
    test=[ord('K'),ord('O'),ord('G'),ord('N'),ord('I'),ord('T'),ord('Y'),ord('W'),ord('I'),ord('S'),ord('T'),ord('Y'),ord('K'),ord('A')]
    różnice=[0*len(populacja)]
    for i in range(len(populacja)):
        for q in range(len(populacja[i])):
            różnice[i]+=math.fabs(test[q]-populacja[i][q])
    return min(różnice)



print(ocena_przystosowania(a))
'''
