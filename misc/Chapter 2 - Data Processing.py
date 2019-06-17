
# coding: utf-8

# # Chapter 2: Processing data for machine learning
# 
# To simplify the code examples in these notebooks, we populate the namespace with functions from numpy and matplotlib:

# In[2]:


get_ipython().run_line_magic('pylab', 'inline')


# ### Converting categorical data to numerical features

# In[26]:
cat_data = array(['male', 'female', 'male', 'male', 'female', 'male', 'female', 'female'])

# In[27]:


def cat_to_num(data):
    categories = unique(data)
    features = []
    for cat in categories:
        binary = (data == cat)
        features.append(binary.astype("int"))
    return features


# In[28]:

cat_data
cat_to_num(cat_data)


# ### Simple feature engineering of the Titanic dataset

# In[23]:


cabin_data = array(["C65", "", "E36", "C54", "B57 B59 B63 B66"])


# In[31]:


def cabin_features(data):
    features = []
    for cabin in data:
        cabins = cabin.split(" ")
        n_cabins = len(cabins)
        # First char is the cabin_char
        try:
            cabin_char = cabins[0][0]
        except IndexError:
            cabin_char = "X"
            n_cabins = 0
        # The rest is the cabin number
        try:
            cabin_num = int(cabins[0][1:]) 
        except:
            cabin_num = -1
        # Add 3 features for each passanger
        features.append( [cabin_char, cabin_num, n_cabins] )
    return features


# In[33]:


cabin_features(cabin_data)


# ### Feature normalization

# In[41]:


num_data = array([1, 10, 0.5, 43, 0.12, 8])


# In[42]:


def normalize_feature(data, f_min=-1, f_max=1):
    d_min, d_max = min(data), max(data)
    factor = (f_max - f_min) / (d_max - d_min)
    normalized = f_min + data*factor
    return normalized, factor


# In[43]:


normalize_feature(num_data)

