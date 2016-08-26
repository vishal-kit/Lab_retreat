
# coding: utf-8

# # Assingment 1 for Lab Retreat
# 
# ### Vishal Gaurav

# import the necessary modules

# In[2]:

import numpy as np
import pylab
import matplotlib.pyplot as plt

get_ipython().magic(u'matplotlib notebook')


# generate the random variables

# In[3]:

x= pylab.rand(1000)
y= pylab.rand(1000)


# Generating the plot

# In[10]:

plt.scatter(x,y)

#saving figure
plt.savefig('scatter_vishal')


# In[ ]:



