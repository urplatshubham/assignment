#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd

#IMPORTING THE REQUIRED LIBRARIES


# In[28]:


pip install Yfinance


# In[31]:


import yfinance as yp


# In[ ]:





# In[62]:


start = '2022-03-01'
end= '2022-03-03'


# In[75]:


df1=pd.read_csv(path);


# In[88]:


ticker='BTCUSTD'


# In[87]:


data=yp.download(ticker,start,end)


# In[92]:


data.tail()


# In[ ]:




