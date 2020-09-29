#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# data = pd.read_csv("./ML/data.csv")
# data.head()

# data.shape

# data.info()

# data.values

# data[data.Age>40].head()

# df=pd.DataFrame(data,columns=['Name','Wage','Value'])
# df

# def value_to_float(x):
#     if type(x)==float or type(x)==int:
#         return x
#     if 'K' in x:
#         if len(x) > 1:
#             return float(x.replace('K',''))*1000
#         return 1000.0
#     if 'M'in x:
#         if len(x) > 1:
#             return float(x.replace('M',''))*1000000
#         return 1000000.0
#     if 'B'in x:
#             return float(x.replace('B',''))*1000000000
#     return 0.0                             
# Wage=df.Wage.replace('[\€,]','',regex=True).apply(value_to_float)
# Value=df.Value.replace('[\€,]','',regex=True).map(value_to_float)
# df['Wage']=Wage
# df['Value']=Value
# df['difference']=df['Value']-df['Wage']
# df.sort_values('difference',ascending=False)

# import seaborn as sns
# #sns.set()
# graph=sns.scatterplot(x='Wage',y='Value',data=df)
# graph;

# from bokeh.plotting import figure, show
# from bokeh.models import HoverTool
# hover = HoverTool(tooltips = [
#     ('index', '$index'),
#     ('(Wage,Value)','(@Wage,@Value)'),
#     ('Name','@Name')])
# p = figure(title = "Soccer 2019", x_axis_label = "Wage",
#            y_axis_label = "Value", plot_width = 700,
#            plot_height = 700, tools = [hover])
# p.circle("Wage","Value",size=10,source=df)
# p.show()

# from sklearn.datasets import load_iris
# iris =load_iris()

# X = iris.data
# y = iris.target
# feature_names= iris.feature_names
# target_names=iris.target_names  

# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)

# from sklearn.neighbors import KNeighborsClassifier
# knn=KNeighborsClassifier(n_neighbors=3)
# knn.fit(X_train,y_train)
# y_pred=knn.predict(X_test)

# from sklearn import metrics
# print(metrics.accuracy_score(y_test,y_pred))
# sample=[[3,5,4,2],[2,3,5,4]]
# predictions=knn.predict(sample)
# print(predictions)
# pred_species=[target_names[p] for p in predictions]
# print('predictions:',pred_species)

# from joblib import dump,load
# dump(knn, filename='./ML/knnmodel.joblib')

# model = load('./ML/knnmodel.joblib')
# model.predict(X_test)
# model.score(X_test, y_test)

# x_index = 0
# y_index = 1
# #formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])
# plt.figure(figsize=(5,4))
# plt.scatter(iris.data[:,0], iris.data[:,1], c=iris.target)
# plt.colorbar(ticks=[0,1,2], format = formatter)
# plt.xlabel(iris.feature_names[x_index])
# plt.ylabel(iris.feature_names[y_index])
# plt.tight_layout()
# plt.show()

# features = iris.data.T
# plt.scatter(features[2], features[3], alpha=0.2, s=100*features[3], c=iris.target, cmap='viridis')
# plt.xlabel(iris.feature_names[2])
# plt.ylabel(iris.feature_names[3])
# plt.colorbar(ticks=[0,1,2], format=formatter)


# In[ ]:




