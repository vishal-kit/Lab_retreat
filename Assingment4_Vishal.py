
# coding: utf-8

# # Lab Retreat
# ### Vishal Gaurav

# In[29]:

#import modules
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import pylab
from sklearn import cluster
get_ipython().magic(u'matplotlib notebook')


# In[6]:

data = np.loadtxt('CodeIQ_data.txt')


# In[15]:

model = cluster.KMeans(n_clusters=3)


# In[16]:

model_fit = model.fit(data)


# In[45]:

plt.scatter(data[:,0],data[:,1],color="R")
plt.scatter(model_fit.cluster_centers_[:,0],model_fit.cluster_centers_[:,1])
plt.savefig('assingment4_vishal')


# In[ ]:




# In[ ]:



