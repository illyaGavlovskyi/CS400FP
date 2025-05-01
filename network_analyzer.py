#pandass  for data analysis
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import csv

dir_name = "csv"
os.listdir(dir_name)
files = [] 
for file in os.listdir(dir_name):
    if file.endswith(".csv"):
        files.append(file)
print("\nCSV files:")
for i in range(len(files)):
    print(f"{i + 1}. {files[i]}")
choice = int(input("\nEnter file you want to load: ")) - 1
file_path = os.path.join(dir_name, files[choice])

#with open(file_path, mode ='r') as file:
#  csvFile = csv.reader(file)
#  for lines in csvFile:
#        print(lines)

df = pd.read_csv(file_path)
dr = pd.read_csv('devices.csv')
# print(df.to_string())
source_counts = df['Source'].value_counts()
destination_counts = df['Destination'].value_counts()
print(source_counts)
print(destination_counts)
print(dr)


