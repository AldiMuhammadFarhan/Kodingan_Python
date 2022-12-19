import pandas as pd
import datetime
import matplotlib.pyplot as plt
'''
apply & lambda biasa digunakan untuk membuat kolom baru, berdasarkan suatu kolom lain yang sudah ada (misal .apply(lambda x: x*2) 
berarti setiap input x di dalam kolom, akan diubah menjadi x*2). Dalam hal ini kolom yang sudah ada adalah dataset['order_date'], 
lalu tiap nilai di dalamnya kita proses agar menjadi month-nya saja

Function datetime.datetime.strptime digunakan untuk mengubah date/time dalam bentuk string menjadi tipe data datetime.

Function  strftime digunakan untuk mengubah format suatu data bertime datetime, dalam hal ini diubah menjadi '%Y-%m', 
yang berarti outputnya adalah waktu dengan bentuk YYYY-MM atau tahun dan bulan saja, tanggalnya sudah tidak ada. 
'''
dataset = pd.read_csv(
    'https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(
    lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))

dataset['gmv'] = dataset['item_price']*dataset['quantity']
print('Ukuran dataset: %d baris dan %d kolom\n' % dataset.shape)
print('Lima data teratas:')
print(dataset.head())

monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()
print(monthly_amount)
'''
 memanggil function plt.plot lalu definisikan nilai di sumbu-x dan sumbu-y. Dalam hal ini, definisikan kolom order_month 
 di sumbu-x (parameter pertama), dan kolom gmv di sumbu-y (parameter kedua). 
 Setelah selesai mendefinisikan komponen chart-nya, lalu panggil plt.show()untuk menampilkan grafiknya.
'''
plt.plot(monthly_amount['order_month'], monthly_amount['gmv'])
plt.show()
# Atau bisa dengan menggunakan fungsi .plot() langsung dari variabel dataframe, yaitu dataset pada kasus kita 
# sebelumnya.
# dataset.groupby(['order_month'])['gmv'].sum().plot()
# plt.show()
