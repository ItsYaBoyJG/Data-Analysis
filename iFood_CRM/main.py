import pandas as pd
import numpy as np
import seaborn
import matplotlib.pyplot as pyplt
from datetime import date
from scipy.cluster.hierarchy import dendrogram, linkage
import csv




f_path = "Data_Sets/iFood_BA_Test/new_ifood_df.csv"

data = pd.read_csv(f_path)

df = pd.DataFrame(data)

marD_length = len(data['marital_Divorced'])
marS_length = len(data['marital_Single'])
marT_length = len(data['marital_Together'])
marW_length = len(data['marital_Widow'])

marD_values = data['marital_Divorced'].values
marS_values = data['marital_Single'].values
marT_values = data['marital_Together'].values
marW_values = data['marital_Widow'].values

data['marital_Divorced'].astype('string')

for index, row in df.iterrows():
    for i in data['marital_Divorced']:
        if i == 1:
           
        
    


#for x in marD_length:
#    if x.values == 0:
        
    




#data['Marital_Status'] = data['marital_Divorced'] + data['marital_Single'] + data['marital_Together'] + data['marital_Widow']

#data['Education'] = data['education_2n Cycle'] + data['education_Basic'] + data['education_Graduation'] +data['education_Master'] + data['education_PhD']

#data.insert(27, 'Marital_Status', [data['Marital_Status']])

#data.insert(28, 'Education', [data['Education']])

#del data['marital_Divorced'], data['marital_Single'], data['marital_Together'], data['marital_Widow'], data['education_2n Cycle'], data['education_Basic'], data['education_Graduation'], data['education_Master'], data['education_PhD']

#data.to_csv(f_path, index= False)

