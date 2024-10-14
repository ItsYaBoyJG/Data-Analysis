import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans


f_path = "Data_Sets/iFood_BA_Test/new_ifood_df.csv"


data = pd.read_csv(f_path)

fig, x_ax = plt.subplots(1,3, figsize=(15,4))

sns.countplot(data['Marital_Status'], ax=x_ax[0])
sns.countplot(data['Education'], ax=x_ax[1])

plot = data.groupby(['Marital_Status', 'Education']).size().reset_index().pivot(columns='Marital_Status', index='Education', values=0)
plot.apply(lambda x: x/x.sum(), axis=1).plot(kind='bar', stacked=True, ax=x_ax[2], colormap='Paired')
plt.legend(loc='center left', bbox_to_anchor=(1.0,0.5))
plt.tight_layout()
fig.show()