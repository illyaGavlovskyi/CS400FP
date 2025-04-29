#pandass  for data analysis
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os 

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

with open('Giants.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)
