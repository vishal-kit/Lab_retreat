
# coding: utf-8

# # Lab Retreat
# ## assingment 5
# #### Vishal Gaurav

# In[8]:

#import modules
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import pylab
from sklearn import svm
get_ipython().magic(u'matplotlib notebook')


# In[6]:

data=pd.read_table("CodeIQ_auth.txt",delimiter=' ',header=None)


# In[9]:

clf = svm.LinearSVC()


# In[39]:

clf.fit(data.iloc[:,:2],data[2])


# In[46]:

data1 =pd.read_table("CodeIQ_mycoins.txt",delimiter=' ',header=None)
c= clf.predict(data1)


# In[48]:

print c


# In[ ]:



