#CONTACT TRACING WITH MACHINE LEARNING
#identify other persons infected
#DBSCAN algorithm-Density based spatial clustering
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
import datetime as dt
from sklearn.cluster import DBSCAN
df = pd.read_csv('result.csv')
df.head()


plt.figure(figsize=(8,8))
sns.scatterplot(x='Latitude', y='Longitude',data=df,hue='User')
plt.legend(bbox_to_anchor= [1, 0.8])
plt.show()


def get_infected_names(input_name):

  epsilon = 0.0018288 
  model=DBSCAN(eps=epsilon, min_samples=2, metric='haversine').fit(df[['Latitude', 'Longitude']])
  df['cluster'] = model.labels_.tolist()

  input_name_clusters = []
  for i in range(len(df)):
      if df['User'][i] == input_name:
          if df['cluster'][i] in input_name_clusters:
              pass
          else:
              input_name_clusters.append(df['cluster'][i])
    
  infected_names = []
  for cluster in input_name_clusters:
      if cluster != -1:
          ids_in_cluster = df.loc[df['cluster'] == cluster, 'User']
          for i in range(len(ids_in_cluster)):
              member_id = ids_in_cluster.iloc[i]
              if (member_id not in infected_names) and (member_id != input_name):
                  infected_names.append(member_id)
              else:
                  pass
  return infected_names



print(get_infected_names('John'))