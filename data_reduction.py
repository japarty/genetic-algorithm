import aseegg as ag
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

myPath = "C:\\Users\\Connor\\Desktop\\thesis\\data"
myFiles=os.listdir(myPath)
for file in myFiles:
    data = pd.read_csv('data\\'+file,header=None)
    new_data=data[[14,21,22,27]].copy()
    new_data.to_csv(r'C:\Users\Connor\Desktop\thesis\new_data\\'+file, index = None, header=True)
