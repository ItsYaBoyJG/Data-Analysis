import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans


f_path = "Data_Sets/iFood_BA_Test/new_ifood_df.csv"


data = pd.read_csv(f_path)

df = pd.DataFrame(f_path)

col_to_move = df.pop('Age')

df.insert(2, 'Age', col_to_move)

df.to_csv(f_path)