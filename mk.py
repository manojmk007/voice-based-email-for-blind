import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data=pd.read_csv(r"file_path")
plt.scatter(data['Longitude'],data['Latitude'])
plt.xlim(-180,180)
plt.ylim(-90,90)
plt.xlabel("Longtitude")
plt.ylabel("Latitude")
plt.show()
x=data.iloc[:,1:3]
kmeans=KMeans(3)
kmeans.fit(x)
identified_clusters=kmeans.fit_predit(x)
data_with_clusters=data.copy()
data_with_clusters['Clusters']=identifed_clusters
plt.scatter(data_with_clusters['Longitude'],data_with_clusters['Latitude'],
c=data_with_clusters['Clusters'],cmap='rainbow')
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
            
