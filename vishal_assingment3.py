
# coding: utf-8

# # Lab Retreat
# ### Vishal Gaurav

# In[1]:

#import modules
import numpy as np
import matplotlib.pyplot as plt
import pylab


# In[2]:

get_ipython().magic(u'matplotlib notebook')


# In[7]:

#x= pylab.rand(1000)
y=[]


# In[8]:

for x in range(-5,5,1):
    y.append(2 * (x**2) - 20)


# In[14]:

x= range(-5,5,1)


# In[18]:

plt.scatter(x,y)
plt.savefig('vishal_assingment3')


# In[ ]:



