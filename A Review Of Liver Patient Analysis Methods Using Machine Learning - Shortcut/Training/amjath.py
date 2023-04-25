# -*- coding: utf-8 -*-
"""amjath.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SNE07YLQ-9pevn6FxCsbgj4bCceJAS5e
"""

import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams 
from scipy import stats

data= pd.read_csv('/content/archive.zip')
data

data.info()

data.isnull().any()

data.isnull().sum()

data['Albumin_and_Globulin_Ratio'].fillna(data['Albumin_and_Globulin_Ratio'].mode()[0], inplace=True)

from sklearn.preprocessing import LabelEncoder
lc = LabelEncoder()
data['Gender']= lc.fit_transform(data['Gender'])

data.describe()

sns.distplot(data['Age'])
plt.title('Age Distribution Graph')
plt.show()

sns.countplot(data=data,x='Gender')

plt.figure(figsize=(10,7))
sns.heatmap(data.corr(),annot=True)

from sklearn.preprocessing import scale
X=data[['Age','Gender','Total_Bilirubin','Direct_Bilirubin','Alkaline_Phosphotase','Alamine_Aminotransferase','Aspartate_Aminotransferase','Total_Protiens','Albumin']]
X_scaled=pd.DataFrame(scale(X),columns=X.columns)
X_scaled.head()

X=data.iloc[:,:-1]
Y=data.Dataset

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X_scaled,Y,test_size=0.2,random_state=42)

pip install imblearn

from imblearn.over_sampling import SMOTE
smote=SMOTE()
Y_train.value_counts()

X_train_smote,Y_train_smote=smote.fit_resample(X_train,Y_train)
Y_train_smote.value_counts()

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
model1=RandomForestClassifier()
model1.fit(X_train_smote, Y_train_smote)
Y_predict=model1.predict(X_test)
rfc1=accuracy_score(Y_test,Y_predict)
rfc1
pd.crosstab(Y_test, Y_predict)
print(classification_report(Y_test,Y_predict))

from sklearn.tree import DecisionTreeClassifier 
model4=DecisionTreeClassifier() 
model4.fit(X_train_smote, Y_train_smote) 
Y_predict=model4.predict(X_test) 
dtc1=accuracy_score (Y_test,Y_predict)
dtc1 
pd.crosstab(Y_test,Y_predict) 
print(classification_report (Y_test,Y_predict))

from sklearn.neighbors import KNeighborsClassifier 
model2=KNeighborsClassifier() 
model2.fit(X_train_smote,Y_train_smote) 
y_predict = model2.predict(X_test) 
knn1=(accuracy_score (Y_test,Y_predict))
knn1 
pd.crosstab(Y_test,Y_predict) 
print(classification_report (Y_test, Y_predict))

from sklearn.linear_model import LogisticRegression 
model5=LogisticRegression() 
model5.fit(X_train_smote, Y_train_smote) 
Y_predict=model5.predict(X_test) 
logi1=accuracy_score(Y_test,Y_predict) 
logi1
pd.crosstab(Y_test,Y_predict) 
print(classification_report (Y_test, Y_predict))

print(X_train.shape)

import tensorflow.keras
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense

#Initialising the ANN 
classifier = Sequential()

# Adding the input Layer and the first hidden Layer 
classifier.add(Dense(units=100, activation='relu', input_dim=10))

# Adding the second hidden layer

classifier.add(Dense (units=50, activation='relu'))

# Adding the output Layer 
classifier.add(Dense (units=1, activation='sigmoid'))

#compiling the ANN
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#fitting the ANN to the training set
model_history=classifier.fit(X_train,Y_train,batch_size=100,validation_split=0.2,epochs=100)

model4.predict([[50,1,1.2,0.8,150,70,80,7.2,3.4]])

model1.predict([[50,1,1.2,0.8,150,70,80,7.2,3.4]])

model2.predict([[50,1,1.2,0.8,150,70,80,7.2,3.4]])

model5.predict([[42,0,1,1.2,0.8,240,70,80,7.2]])

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

Y_pred = (Y_pred > 0.5)
Y_pred

def predict_exit(sample_value):
# Convert list to numpy array 
   sample_value = np.array (sample_value)
# Reshape because sample value contains only 1 record 
   sample_value = sample_value.reshape(1, -1)
#Feature Scaling
   sample_value = scale(sample_value)
   return classifier.predict(sample_value)
#Age Gender Total Bilrubin Direct Bilrubin Alkaline Phosphotase
sample_value = [[50,1,1.2,0.8,150,70,80,7.2,3.4,0.8]]
if predict_exit (sample_value)>0.5:
   print('Prediction: Liver Patient')
else:
   print('Prediction: Healthy ')

acc_smote= [['KNN Classifier', knn1], ['RandomForestClassifier', rfc1],
['DecisionTreeClassifier', dtc1], ['Logistic Regression', logi1]] 
Liverpatient_pred= pd.DataFrame(acc_smote, columns = ['classification models', 'accuracy_score'])
Liverpatient_pred

plt.figure(figsize=(7,5))
plt.xticks(rotation=90)
plt.title('Classification models & accuracy scores after SMOTE', fontsize=18)
sns.barplot(x="classification models",y="accuracy_score", data=Liverpatient_pred, palette ="Set2")

import pandas as pd

X = pd.DataFrame(X)
X = X.dropna()

import numpy as np

nan_mask = np.isnan(X)
X = X[~np.any(nan_mask, axis=1)]  # remove rows with NaN values

from sklearn.ensemble import ExtraTreesClassifier

model = ExtraTreesClassifier()
model.fit(X, Y)

model.feature_importances_

X = pd.DataFrame(X)  # Convert X to a pandas DataFrame
dd = pd.DataFrame(model.feature_importances_, index=X.columns).sort_values(0, ascending=False)
dd

dd.plot(kind='barh', figsize=(7,6)) 
plt.title("FEATURE IMPORTANCE", fontsize=14)