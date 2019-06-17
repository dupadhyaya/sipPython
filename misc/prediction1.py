
# coding: utf-8

# # Chapter 3 - Modeling and prediction

# In[2]:
import numpy as np
import pandas as pd

get_ipython().run_line_magic('pylab', 'inline')


# ### The Titanic dataset
# 
# We use the Pandas library to import the Titanic survival dataset.

# In[27]:


#import pandas
data = pd.read_csv("data/titanic.csv")
data.loc[[:5]]


# In[30]:


# We make a 80/20% train/test split of the data
data_train = data[:int(0.8*len(data))]
data_test = data[int(0.8*len(data)):]


# ### Preparing the data

# In[46]:


# The categorical-to-numerical function from chapter 2
# Changed to automatically add column names
def cat_to_num(data):
    categories = unique(data)
    features = {}
    for cat in categories:
        binary = (data == cat)
        features["%s=%s" % (data.name, cat)] = binary.astype("int")
    return pandas.DataFrame(features)


# In[57]:


def prepare_data(data):
    """Takes a dataframe of raw data and returns ML model features
    """
    
    # Initially, we build a model only on the available numerical values
    features = data.drop(["PassengerId", "Survived", "Fare", "Name", "Sex", "Ticket", "Cabin", "Embarked"], axis=1)
    
    # Setting missing age values to -1
    features["Age"] = data["Age"].fillna(-1)
    
    # Adding the sqrt of the fare feature
    features["sqrt_Fare"] = sqrt(data["Fare"])
    
    # Adding gender categorical value
    features = features.join( cat_to_num(data['Sex']) )
    
    # Adding Embarked categorical value
    features = features.join( cat_to_num(data['Embarked']) )
    
    return features


# ### Building a logistic regression classifier with Scikit-Learn

# In[58]:


#cat_to_num(data['Sex'])
features = prepare_data(data_train)
features[:5]


# In[59]:


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(features, data_train["Survived"])


# In[60]:


# Make predictions
model.predict(prepare_data(data_test))


# In[64]:


# The accuracy of the model on the test data
# (this will be introduced in more details in chapter 4)
model.score(prepare_data(data_test), data_test["Survived"])


# ### Non-linear model with Support Vector Machines

# In[62]:


from sklearn.svm import SVC
model = SVC()
model.fit(features, data_train["Survived"])


# In[63]:


model.score(prepare_data(data_test), data_test["Survived"])


# ### Classification with multiple classes: hand-written digits
# 
# We use the popular non-linear multi-class K-nearest neighbor algorithm to predict hand-written digits from the MNIST dataset.
# 

# In[65]:


mnist = pandas.read_csv("data/mnist_small.csv")
mnist_train = mnist[:int(0.8*len(mnist))]
mnist_test = mnist[int(0.8*len(mnist)):]


# In[66]:


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(mnist_train.drop("label", axis=1), mnist_train['label'])


# In[71]:


preds = knn.predict_proba(mnist_test.drop("label", axis=1))
pandas.DataFrame(preds[:5], index=["Digit %d"%(i+1) for i in range(5)])


# In[73]:


knn.score(mnist_test.drop("label", axis=1), mnist_test['label'])


# ### Predicting numerical values with a regression model
# 
# We use the the Linear Regression algorithm to predict miles-per-gallon of various automobiles.

# In[79]:


auto = pandas.read_csv("data/auto-mpg.csv")

# Convert origin to categorical variable
auto = auto.join(cat_to_num(auto['origin']))
auto = auto.drop('origin', axis=1)

# Split in train/test set
auto_train = auto[:int(0.8*len(auto))]
auto_test = auto[int(0.8*len(auto)):]

auto[:5]


# In[80]:


from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(auto_train.drop('mpg', axis=1), auto_train["mpg"])


# In[83]:


pred_mpg = reg.predict(auto_test.drop('mpg',axis=1))


# In[89]:


plot(auto_test.mpg, pred_mpg, 'o')
x = linspace(10,40,5)
plot(x, x, '-');

