import aseegg as ag
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import math

new_features=[]
numbers=['0','1','2','3','4','5','6','7','8','9']

myPath = "C:\\Users\\Connor\\Desktop\\thesis\\tested_data"
myFiles=os.listdir(myPath)

a = []

for i in myFiles:
    if "Trial5" in i:
        a.append(i)
myFiles = a


col_names=[]
electrodes = ['14','21','22','27']
col_types=['LAT','AMP','LAR','AAMP','ALAR','PAR','NAR','TAR','ATAR','TAAR']
for freq in electrodes:
    for col_type in col_types:
        col_names.append(freq+'_'+col_type)
col_names.append('target')


for file in myFiles:
    data = pd.read_csv('tested_data\\'+file)
    new_features.append([])
    for i in data:
        signal = ag.pasmowoprzepustowy(ag.pasmowozaporowy(data[i], 256, 49, 51), 256, 1, 50)
        signal = signal[1280:1280+256]
        print(signal[:10])
        AMP = np.amax(signal)
        LAT = int(np.where(signal == AMP)[0][0])+1
        LAR = float(AMP/LAT)
        AAMP = 0
        ALAR = math.fabs(LAR)
        PAR = 0
        NAR = 0
        TAR = 0
        TAAR = 0
        for amp_index in range(len(signal)):
            if math.fabs(signal[amp_index])>AAMP:
                AAMP = math.fabs(signal[amp_index])
            if signal[amp_index]>0:
                PAR += signal[amp_index]
            elif signal[amp_index]<0:
                NAR += signal[amp_index]
            TAR += signal[amp_index]
            TAAR += math.fabs(signal[amp_index])
        ATAR = math.fabs(TAR)
        target = file[6:8] if file[7:8] in numbers else file[6:7]

        new_features[-1].append(LAT)
        new_features[-1].append(int(AMP))
        new_features[-1].append(LAR)
        new_features[-1].append(AAMP)
        new_features[-1].append(ALAR)
        new_features[-1].append(PAR)
        new_features[-1].append(NAR)
        new_features[-1].append(TAR)
        new_features[-1].append(ATAR)
        new_features[-1].append(TAAR)
    new_features[-1].append(target)

features = pd.DataFrame(new_features, columns = col_names)
print(features)
features.to_csv(r'C:\Users\Connor\Desktop\thesis\\'+'features.csv', index = None, header=True)

        # print(AMP)
        # t=np.linspace(0,len(data[i])/256,len(data[i]))
        # plt.subplot(2,1,1)
        # plt.plot(t,data[i])
        # przefiltrowany_sygnal= ag.pasmowoprzepustowy(ag.pasmowozaporowy(data[i], 256, 49, 51), 256, 1, 50)
        # plt.subplot(2,1,2)
        # plt.plot(t,przefiltrowany_sygnal)
        # plt.show()



    #for i in data:
    #    data[i]=przefiltrowany_sygnal= ag.pasmowoprzepustowy(ag.pasmowozaporowy(data[i], 256, 49, 51), 256, 1, 50)
    #data.to_csv(r'C:\Users\Connor\Desktop\thesis\data_after_filtration\\'+file, index = None, header=True)

#filtrowanie
#przefiltrowany_sygnal= ag.pasmowoprzepustowy(ag.pasmowozaporowy(data['1'], 200, 49, 51), 200, 1, 50)

#wykrycie mrugnięcia oraz print wyniku (zdekodowanie informacji)
#print([data['liczba'][i] for i in range(1,len(przefiltrowany_sygnal)) if przefiltrowany_sygnal[i]>=0.1 and przefiltrowany_sygnal[i-1]<0.1])
