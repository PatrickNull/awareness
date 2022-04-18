import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier

# 生成训练集和测试集数据，‘ISCX_Botnet-Training.pcap_Flow1.csv’中数据只判断是否是僵尸网络，‘ISCX_Botnet-Training.pcap_Flow2.csv’中对僵尸网络的协议类型做了判断
# data_train = pd.read_csv("ISCX_Botnet-Training.pcap_Flow1.csv", encoding="gb2312")
# x_train = data_train[['Flow Duration','Pkt Size Avg','Flow Byts/s','Pkt Len Mean','Fwd Header Len','Bwd Header Len']]#,'Down/Up Ratio'
# y_train = data_train['Label']

# data_test = pd.read_csv("ISCX_Botnet-Testing.pcap_Flow1.csv", encoding="gb2312")
# x_test = data_test[['Flow Duration','Pkt Size Avg','Flow Byts/s','Pkt Len Mean','Fwd Header Len','Bwd Header Len']]#,'Down/Up Ratio'
# y_test = data_test['Label']

# 因为原本的训练集和测试集效果不是很好，所以将训练集和测试集合并并从中按比例随机分配新的训练集和测试集
data = pd.read_csv("ISCX_Botnet.pcap_Flow2.csv", encoding="gb2312")
x = data[['Flow Duration','Pkt Size Avg','Pkt Len Mean','Flow Byts/s','Fwd Header Len','Bwd Header Len','Down/Up Ratio']]#
y = data['Label']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.5)# 对半分，一半训练一半测试

print(type(y_test))
for i in y_test:
    print(i)
# clf = DecisionTreeClassifier()#criterion="gini", min_samples_leaf=10
# clf.fit(x_train,y_train)
# result = clf.predict(x_test)
# print(clf.score(x_test,y_test))
# for i in range(len(result)):
#     print(result[i])