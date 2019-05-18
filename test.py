#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sentiment import load_model


# In[2]:


vocab =7000
sentence = 500
embedding = 300


# In[4]:


model = load_model(vocab_length=vocab,sentence_length=sentence,embedding_length=embedding)


# In[5]:


model.summary()


# In[ ]:




