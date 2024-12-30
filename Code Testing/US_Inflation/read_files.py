import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplt


#file path
file_path = "Data_Sets/US_Inflation/cpi_data.csv"


#load data
data = pd.read_csv(file_path)


print(data.head())