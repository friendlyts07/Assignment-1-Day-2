#!/usr/bin/env python
# coding: utf-8

# # Dictonary

# In[1]:


mydict = {'first_name': 'Tirth', 'last_name': 'shah', 'age': 20, 'sem': 6, 'favorite_color': 'blue'}


# In[2]:


mydict


# In[3]:


mydict.setdefault("age")


# In[4]:


mydict.items()


# In[6]:


mydict.pop("sem")


# In[8]:


mydict


# In[10]:


newmydict={'favorite_color': 'white'}
mydict.update(newmydict)


# In[11]:


mydict


# In[12]:


mydict.get('last_name')


# In[13]:


mydict.values()


# In[ ]:




