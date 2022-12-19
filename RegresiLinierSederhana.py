# load libary
import pandas as pd
import statsmodels.api as sm

# load data
raw_data = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=(";"))

# lihat data
# print(raw_data)

# Variabel tak bebas
nilai_Y = raw_data[['Total']]
# Variabel bebas
nilai_X = sm.add_constant(raw_data['Pendapatan'])
# Membuat model regresi linier
model_regresi = sm.OLS(endog=nilai_Y , exog=nilai_X).fit()
print(model_regresi.summary())