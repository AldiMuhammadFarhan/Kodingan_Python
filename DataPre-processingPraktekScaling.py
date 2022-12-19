# untuk memberi range nilai yang sama
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
dataset = pd.read_csv(
    'https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')
dataset.fillna(dataset.mean(), inplace=True)

# Define MinMaxScaler as scaler
scaler = MinMaxScaler()
# list all the feature that need to be scaled
scaling_column = ['Administrative', 'Administrative_Duration', 'Informational', 'Informational_Duration',
                  'ProductRelated', 'ProductRelated_Duration', 'BounceRates', 'ExitRates', 'PageValues']
'''
jika semua data numerik baris code di atas sudah cukup untuk memprosesnya , namun jika tercampur atau bukan numerik
harus di transform / di ubah ke numerik
'''
# Apply fit_transfrom to scale selected feature
dataset[scaling_column] = scaler.fit_transform(dataset[scaling_column])
# Cheking min and max value of the scaling_column
print(dataset[scaling_column].describe().T[['min', 'max']])
