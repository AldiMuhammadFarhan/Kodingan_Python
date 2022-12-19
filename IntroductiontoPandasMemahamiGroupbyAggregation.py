'''Groupby memiliki konsep untuk

Split: melakukan indexing/multi-indexing dengan apa yang di specify as groupby menjadi kelompok
Apply: menerapkan fungsi pada masing-masing kelompok tersebut
Combine: mengumpulkan semua hasil fungsi dari tiap kelompok kembali menjadi dataframe
 '''
import pandas as pd
# Load data global_air_quality.csv
global_air_quality = pd.read_csv(
    'https://storage.googleapis.com/dqlab-dataset/LO4/global_air_quality_4000rows.csv')
print('Lima data teratas:\n', global_air_quality.head())
# Melakukan pengecekan terhadap data
print('Info global_air_quality:\n', global_air_quality.info())
# Melakukan count tanpa groupby
print('Count tanpa groupby:\n', global_air_quality.count())
# Melakukan count dengan groupby
gaq_groupby_count = global_air_quality.groupby('source_name').count()
print('Count dengan groupby (5 data teratas):\n', gaq_groupby_count.head())
'''perbedaan antara melakukan count dengan groupby dan tanpa groupby,

Terdapat index apa yang di specify as groupby
Perhitungan jadi berdasarkan apa yang di specify as groupby
Overall, lebih mudah untuk membaca data summary yang telah di groupby'''


'''menerapkan groupby dan fungsi aggregasi mean dan std untuk menentukan nilai rata-rata dan standar deviasi dari 
masing-masing kelompok data'''
# Load data global_air_quality.csv
gaq = pd.read_csv(
    'https://storage.googleapis.com/dqlab-dataset/LO4/global_air_quality_4000rows.csv')
# Create variabel pollutant 
pollutant = gaq[['country', 'city', 'pollutant', 'value']].pivot_table(
    index=['country', 'city'], columns='pollutant').fillna(0)
print('Data pollutant (5 teratas):\n', pollutant.head())
'''[1] Group berdasarkan country dan terapkan aggregasi mean, method .mean() setelah penerapan method .groupby() 
digunakan untuk mencari rata-rata dari tiap kelompok'''
# [1] Group berdasarkan country dan terapkan aggregasi mean
pollutant_mean = pollutant.groupby('country').mean()
print('Rata-rata pollutant (5 teratas):\n', pollutant_mean.head())
'''[2] Group berdasarkan country dan terapkan aggregasi std, method .std() setelah penerapan method .groupby() 
digunakan untuk mencari standard deviasi (penyimpangan) dari tiap kelompok'''
# [2] Group berdasarkan country dan terapkan aggregasi std
pollutant_std = pollutant.groupby('country').std().fillna(0)
print('Standar deviasi pollutant (5 teratas):\n', pollutant_std.head())
'''[3] Group berdasarkan country dan terapkan aggregasi sum, method .sum() setelah penerapan method .groupby() 
digunakan untuk mencari total nilai dari tiap kelompok'''
# [3] Group berdasarkan country dan terapkan aggregasi sum
pollutant_sum = pollutant.groupby('country').sum()
print('Total pollutant (5 teratas):\n', pollutant_sum.head())
'''[4] Group berdasarkan country dan terapkan aggregasi nunique, method .nunique() setelah penerapan method 
.groupby() digunakan untuk mencari berapakah jumlah unique value dari tiap kelompok'''
# [4] Group berdasarkan country dan terapkan aggregasi nunique
pollutant_nunique = pollutant.groupby('country').nunique()
print('Jumlah unique value pollutant (5 teratas):\n', pollutant_nunique.head())
'''[5] Group berdasarkan country dan terapkan aggregasi min, method .min() setelah penerapan method .groupby() 
digunakan untuk memunculkan nilai terkecil dari tiap kelompok'''
# Group berdasarkan country dan terapkan aggregasi first
pollutant_first = pollutant.groupby('country').min()
print('Item pertama pollutant (5 teratas):\n', pollutant_first.head())
'''[6] Group berdasarkan country dan terapkan aggregasi max, method .max() setelah penerapan method .groupby() 
digunakan untuk memunculkan nilai terbesar dari tiap kelompok'''
# Group berdasarkan country dan terapkan aggregasi last
pollutant_last = pollutant.groupby('country').max()
print('Item terakhir pollutant (5 teratas):\n', pollutant_last.head())
'''Gunakanlah method .first() dan .last() untuk aggregasi setelah penerapan .groupby() yang masing-masingnya 
bertujuan untuk memunculkan item pertama dan item terakhir dari tiap kelompok.'''
# Group berdasarkan country dan terapkan aggregasi first
pollutant_first = pollutant.groupby('country').first()
print('Item pertama pollutant (5 teratas):\n', pollutant_first.head())
# Group berdasarkan country dan terapkan aggregasi last
pollutant_last = pollutant.groupby('country').last()
print('Item terakhir pollutant (5 teratas):\n', pollutant_last.head())


'''menggunakan grouby dengan multiple aggregations yang berupa kombinasi antara beberapa fungsi'''
# Group berdasarkan country dan terapkan aggregasi: min, median, mean, max
multiagg = pollutant.groupby('country').agg(['min', 'median', 'mean', 'max'])
print('Multiple aggregations (5 teratas):\n', multiagg.head())


'''Tentukanlah inter quartile range (IQR) pada setiap kelompok data, dan kemudian tampilkanlah 5 data teratas saja.'''
# Create sebuah function: iqr


def iqr(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    return Q3 - Q1


# Group berdasarkan country dan terapkan aggregasi dari function: iqr
custom_agg = pollutant.groupby('country').agg(iqr)
print('Custom aggregation (5 teratas):\n', custom_agg.head())


'''Penggunaan custom aggregation lainnya pada dataframe yang telah digroupby dapat dilakukan dengan mempasskan 
sebuah dict yang berisi 'key' dict sebagai nama kolomnya dan 'value' dict adalah fungsi untuk aggregasi, baik user 
defined function atau yang telah tersedia.'''
# Function IQR
def iqr(series):
	return series.quantile(0.75) - series.quantile(0.25)
# Create custom aggregation using dict
custom_agg_dict = pollutant['value'][['pm10','pm25','so2']].groupby('country').agg({
   'pm10':'median',
   'pm25':iqr,
   'so2':iqr
})
print('\nCetak 5 data teratas custom_agg_dict:\n', custom_agg_dict.head())
