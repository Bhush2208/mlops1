import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('/content/mlops1/data/Iris.csv')
features = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
target = ['Species']
X_train,X_test,y_train,y_test = train_test_split(df[features],df[target],test_size=0.20,shuffle=True)

clf = DecisionTreeClassifier(criterion = 'entropy')
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)




print(f'Accuracy of the model is {accuracy_score(y_test,y_pred)*100}')
