# Training model : fit
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
dataset = pd.read_csv(
    'https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')
dataset.fillna(dataset.mean(), inplace=True)

LE = LabelEncoder()
dataset['Month'] = LE.fit_transform(dataset['Month'])
LE = LabelEncoder()
dataset['VisitorType'] = LE.fit_transform(dataset['VisitorType'])
X = dataset.drop(['Revenue'], axis=1)
y = dataset['Revenue']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

# Call the classifier
model = DecisionTreeClassifier()
# Fit the classifier to the training data
model = model.fit(X_train, y_train)

# Training model : Predict
# Apply the classifier/model to the test data
y_pred = model.predict(X_test)
print(y_pred.shape)

# Evaluasi model Perfomance

# evaluating the model
print('Training Accuracy :', model.score(X_train, y_train))
print('Testing Accuracy :', model.score(X_test, y_test))

# confusion matrix
# menampilkan confusion matrix cukup menggunakan fungsi confusion_matrix() dari Scikit-Learn
print('\nConfusion matrix:')
cm = confusion_matrix(y_test, y_pred)
print(cm)

# classification report
# gunakan  fungsi classification_report() untuk memunculkan hasil perhitungan metrik - metrik tersebut
'''
Jika mau hitung
Accuracy = (TP + TN ) / (TP+FP+FN+TN)
Precision = (TP) / (TP+FP)
Recall = (TP) / (TP + FN)
F1 Score = 2 * (Recall*Precission) / (Recall + Precission)
'''
print('\nClassification report:')
cr = classification_report(y_test, y_pred)
print(cr)
