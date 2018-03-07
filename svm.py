import sklearn
from sklearn import svm
from random import shuffle
import pandas as pd
import pickle
data = pd.read_csv('/home/james/PycharmProjects/car/car2.csv', encoding='gbk')
data = data.as_matrix()  # 转换为矩阵
shuffle(data)  # 随机打乱数据
data_train = data[:int(0.8*len(data)), :]  # 取前80%为训练数据
data_test = data[int(0.8*len(data)):, :]  # 取后20%为测试数据
x_train = data_train[:, :6]
y_train = data_train[:, 6:]
x_test = data_test[:, :6]
y_test = data_test[:, 6:]
model = svm.SVC()
model.fit(x_train, y_train.ravel())  # 训练分类器  不加.ravel(）会有warning
y_pred_1= model.predict(x_train)
print(sklearn.metrics.accuracy_score(y_train,y_pred_1))  # metrics 度量
y_pred_2 = model.predict(x_test)
print(sklearn.metrics.accuracy_score(y_test,y_pred_2))