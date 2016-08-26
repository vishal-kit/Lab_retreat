
# coding: utf-8

# In[4]:

import numpy as np
import matplotlib.pyplot as plt
import pylab

get_ipython().magic(u'matplotlib notebook')
y=[]

for x in range(-5,5,1):
    y.append(2 * (x**2) - 20)
             
x=range(-5,5,1)

plt.plot(x,y)
plt.savefig('tamaki_Assingment3')


# In[ ]:



