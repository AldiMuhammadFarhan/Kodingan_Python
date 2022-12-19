import numpy as np
import pandas as pd
# File CSV
df_csv = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
print(df_csv.head(3))  # Menampilkan 3 data teratas
# File TSV
df_tsv = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep='\t')
print(df_tsv.head(3))  # Menampilkan 3 data teratas
# File xlsx dengan data di sheet "test"
df_excel = pd.read_excel(
    "https://storage.googleapis.com/dqlab-dataset/sample_excel.xlsx", sheet_name="test")
print(df_excel.head(4))  # Menampilkan 4 data teratas
# File JSON
url = "https://storage.googleapis.com/dqlab-dataset/covid2019-api-herokuapp-v2.json"
df_json = pd.read_json(url)
print(df_json.head(10))  # Menampilkan 10 data teratas


# Baca file sample_csv.csv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
# Tampilkan 3 data teratas
print("Tiga data teratas:\n", df.head(3))
# Tampilkan 3 data terbawah
print("Tiga data terbawah:\n", df.tail(3))


# Baca file TSV sample_tsv.tsv
df = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="\t")
# Index dari df
print("Index:", df.index)
# Column dari df
print("Columns:", df.columns)


# Baca file TSV sample_tsv.tsv
df = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="\t")
# Set multi index df
df_x = df.set_index(['order_date', 'city', 'customer_id'])
# Print nama dan level dari multi index
for name, level in zip(df_x.index.names, df_x.index.levels):
    print(name, ':', level)
# Index dari df_x
print("Index df_x:", df_x.index)


# Baca file sample_tsv.tsv untuk 10 baris pertama saja
df = pd.read_csv(
    "https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="\t", nrows=10)
# Cetak data frame awal
print("Dataframe awal:\n", df)
# Set index baru
df.index = ["pesanan ke-" + str(i) for i in range(1, 11)]
# Cetak data frame dengan index baru
print("Dataframe dengan index baru:\n", df)


# Baca file sample_tsv.tsv dan set lah index_col sesuai instruksi
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv",
                 sep="\t", index_col=["order_date", "order_id"])
# Cetak data frame untuk 8 data teratas
print("Dataframe:\n", df.head(8))


# Baca file sample_csv.csv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
# Slice langsung berdasarkan kolom
df_slice = df.loc[(df["customer_id"] == "18055") &
                  (df["product_id"].isin(
                      ["P0029", "P0040", "P0041", "P0116", "P0117"]))
                  ]
print("Slice langsung berdasarkan kolom:\n", df_slice)


# Baca file sample_csv.csv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
# Set index dari df sesuai instruksi
df = df.set_index(["order_date", "order_id", "product_id"])
# Slice sesuai intruksi
df_slice = df.loc[("2019-01-01", 1612339, ["P2154", "P2159"]), :]
print("Slice df:\n", df_slice)


# Baca file sample_csv.csv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
# Tampilkan tipe data
print("Tipe data df:\n", df.dtypes)
# Ubah tipe data kolom order_date menjadi datetime
df["order_date"] = pd.to_datetime(df["order_date"])
# Tampilkan tipe data df setelah transformasi
print("\nTipe data df setelah transformasi:\n", df.dtypes)


# Baca file sample_csv.csv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
# Tampilkan tipe data
print("Tipe data df:\n", df.dtypes)
# Ubah tipe data kolom quantity menjadi tipe data numerik float
df["quantity"] = pd.to_numeric(df["quantity"], downcast="float")
# Ubah tipe data kolom city menjadi tipe data category
df["city"] = df["city"].astype("category")
# Tampilkan tipe data df setelah transformasi
print("\nTipe data df setelah transformasi:\n", df.dtypes)


# Baca file sample_csv.csv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
# Cetak 5 baris teratas kolom brand
print("Kolom brand awal:\n", df["brand"].head())
# Gunakan method apply untuk merubah isi kolom menjadi lower case
df["brand"] = df["brand"].apply(lambda x: x.lower())
# Cetak 5 baris teratas kolom brand
print("Kolom brand setelah apply:\n", df["brand"].head())
# Gunakan method map untuk mengambil kode brand yaitu karakter terakhirnya
df["brand"] = df["brand"].map(lambda x: x[-1])
# Cetak 5 baris teratas kolom brand
print("Kolom brand setelah map:\n", df["brand"].head())


# number generator, set angka seed menjadi suatu angka, bisa semua angka, supaya hasil random nya selalu sama ketika kita run
np.random.seed(1234)
# create dataframe 3 baris dan 4 kolom dengan angka random
df_tr = pd.DataFrame(np.random.rand(3, 4))
# Cetak dataframe
print("Dataframe:\n", df_tr)
# Cara 1 dengan tanpa define function awalnya, langsung pake fungsi anonymous lambda x
df_tr1 = df_tr.applymap(lambda x: x**2 + 3*x + 2)
print("\nDataframe - cara 1:\n", df_tr1)
# Cara 2 dengan define function
def qudratic_fun(x):
    return x**2 + 3*x + 2
df_tr2 = df_tr.applymap(qudratic_fun)
print("\nDataframe - cara 2:\n", df_tr2)


