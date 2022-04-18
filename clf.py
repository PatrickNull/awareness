import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier

# data_train = pd.read_csv("ISCX_Botnet-Training.pcap_Flow1.csv", encoding="gb2312")
# x_train = data_train[['Flow Duration','Pkt Size Avg','Flow Byts/s','Pkt Len Mean','Fwd Header Len','Bwd Header Len']]#,'Down/Up Ratio'
# y_train = data_train['Label']

# data_test = pd.read_csv("ISCX_Botnet-Testing.pcap_Flow1.csv", encoding="gb2312")
# x_test = data_test[['Flow Duration','Pkt Size Avg','Flow Byts/s','Pkt Len Mean','Fwd Header Len','Bwd Header Len']]#,'Down/Up Ratio'
# y_test = data_test['Label']

data = pd.read_csv("ISCX_Botnet.pcap_Flow2.csv", encoding="gb2312")
x = data[['Flow Duration','Pkt Size Avg','Flow Byts/s','Pkt Len Mean','Fwd Header Len','Bwd Header Len','Down/Up Ratio']]#
y = data['Label']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.5)

print(type(y_test))
for i in y_test:
    print(i)
# clf = DecisionTreeClassifier()#criterion="gini", min_samples_leaf=10
# clf.fit(x_train,y_train)
# result = clf.predict(x_test)
# print(clf.score(x_test,y_test))
# for i in range(len(result)):
#     print(result[i])