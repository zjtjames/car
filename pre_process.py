
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.read_csv('/home/james/PycharmProjects/car/car.csv')


# In[3]:


print(df.shape)


# In[4]:


buyingMaping = {'vhigh':0, 'high':1, 'med':2, 'low':3}
df['buying'] = df['buying'].map(buyingMaping)


# In[5]:


maintMaping = {'vhigh':0, 'high':1, 'med':2, 'low':3}
df['maint'] = df['maint'].map(maintMaping)


# In[6]:


doorsMaping = {'2':2,'3':3,'4':4,'5more':5}
df['doors'] = df['doors'].map(doorsMaping)


# In[7]:


personsMaping = {'2':2,'4':4,'more':4}    
df['persons'] = df['persons'].map(personsMaping)


# In[8]:


lug_bootMapping = {'small':0, 'med':1, 'big':2}
df['lug_boot'] = df['lug_boot'].map(lug_bootMapping)
safetyMapping = {'low':0, 'med':1, 'high':2}
df['safety'] = df['safety'].map(safetyMapping)
classMapping = {'unacc':0,'acc':1,'good':2,'vgood':3}
df['class'] = df['class'].map(classMapping)


# In[9]:


df.to_csv('/home/james/PycharmProjects/car/car2.csv',index=False)


# In[10]:


# df = pd.read_csv('./car1.csv')
# df = df.as_matrix()
# data_train = df[:int(0.8*len(df)),:]
# data_test = df[int(0.8*len(df)):,:]


# In[11]:


#构造特征和标签
# x_train = data_train[:,0:4]
# y_train = data_train[:,5].astype(int)
# x_test = data_test[:,0:4]
# y_test = data_test[:,5].astype(int)
#
#
# # In[12]:
#
#
# #导入模型相关的函数，建立并且训练模型
# from sklearn import svm
# model = svm.SVC()
# model.fit(x_train,y_train)
# import pickle
# #最后一句保存模型，加载模型使用pickle.load('path','rb')
# pickle.dump(model,open('./tmp/svm.model','wb'))
#
#
# # In[15]:
#
#
# from sklearn import metrics
# #训练样本的混淆矩阵
# cm_train = metrics.confusion_matrix(y_train,model.predict(x_train))
# #测试样本的混淆矩阵
#
# cm_test = metrics.confusion_matrix(y_test,model.predict(x_test))
# print(cm_train.shape)
# #保存结果
# pd.DataFrame(cm_train, index = range(1,4),columns = range(1,4)).to_excel('./output/1.xlsx')
# pd.DataFrame(cm_test,index = range(1,4),columns = range(1,4)).to_excel('./output/2.xlsx')


