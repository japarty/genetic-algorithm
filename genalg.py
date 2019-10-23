import random
import math

def populacja(ile_osobnikow,ile_chromosomow):
    populacja=[]
    for i in range(ile_osobnikow):
        populacja.append([])
        for q in range(ile_chromosomow):
            populacja[i].append(random.randint(65,90))
    return populacja

def ocena_przystosowania(populacja):
    test=[ord('K'),ord('O'),ord('G'),ord('N'),ord('I'),ord('T'),ord('Y'),ord('W'),ord('I'),ord('S'),ord('T'),ord('Y'),ord('K'),ord('A')]
    różnice=[0]*len(populacja)
    for i in range(len(populacja)):
        for q in range(len(populacja[i])):
            różnice[i]+=int(math.fabs(test[q]-populacja[i][q]))
    return min(różnice)

def suma_przystosowania(populacja):
    test=[ord('K'),ord('O'),ord('G'),ord('N'),ord('I'),ord('T'),ord('Y'),ord('W'),ord('I'),ord('S'),ord('T'),ord('Y'),ord('K'),ord('A')]
    różnice=[0]*len(populacja)
    for i in range(len(populacja)):
        for q in range(len(populacja[i])):
            różnice[i]+=int(math.fabs(test[q]-populacja[i][q]))
    return sum(różnice)

def ruletka(populacja):
    suma_różnic=suma_przystosowania(populacja)
    kolo=[]
    for i in range(len(populacja)):
        if i==0: poprzednia=0
        else: poprzednia=kolo[i-1]
        kolo.append(poprzednia+(ocena_przystosowania([populacja[i]])/suma_różnic))
    print(kolo)
    nowa_populacja=[]
    for i in populacja:
        loteria=random.uniform(0, 1)
        print(loteria)
        for q in range(len(kolo)):
            if loteria<=kolo[q]:
                nowa_populacja.append(populacja[q])
                print(nowa_populacja)
                break
    return(nowa_populacja)


populacja=populacja(8,14)
print(populacja)
'''
while ocena_przystosowania(populacja)>0:
    populacja=ruletka(populacja)
'''
populacja=ruletka(populacja)
