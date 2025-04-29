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
print(files)