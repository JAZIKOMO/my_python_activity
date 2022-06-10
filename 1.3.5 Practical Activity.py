#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Solution 1: 
from datetime import time 
t = time(14, 42, 5, 566)
# if you type in 05 instead of 5 seconds, you will get an error

print("hour =", t.hour)
print("minute =", t.minute)
print("second =", t.second)
print("microsecond =", t.microsecond)


# In[5]:


# Solution 2: 
from datetime import datetime

dt = datetime(2019, 1, 28, 23, 55, 59, 1023)
print("year =", dt.year)
print("month =", dt.month)
print("day =", dt.day)
print("hour =", dt.hour)
print("minute =", dt.minute)
print("seconds =", dt.second)
print("microsecond =", dt.microsecond)


# In[6]:


# solution 3
from datetime import date

# Date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


# In[8]:


# solution 4
from datetime import datetime

day = datetime(2017, 1, 28)
# This is the code to return the full day name
day.strftime('%A') 


# In[ ]:




