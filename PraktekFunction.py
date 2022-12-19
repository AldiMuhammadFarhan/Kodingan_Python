# Data properti
tabel_properti = {
    'luas_tanah': [70, 70, 70, 100, 100, 100, 120, 120, 150, 150],
    'luas_bangunan': [50, 60, 60, 50, 70, 70, 100, 80, 100, 90],
    'jarak': [15, 30, 55, 30, 25, 50, 20, 50, 50, 15],
    'harga': [500, 400, 300, 700, 1000, 650, 2000, 1200, 1800, 3000]
}
# Dua buah data yang tersimpan dalam tipe list
data1 = [70, 70, 70, 100, 100, 100, 120, 120, 150, 150]
data2 = [50, 60, 60, 50, 70, 70, 100, 80, 100, 90]
# Definisikan fungsi hitng_rata_rata


def hitung_rata_rata(data):
    jumlah = 0
    for item in data:
        jumlah += item
    rata_rata = jumlah/len(data)
    return rata_rata
# Definisikan fungsi hitung_standar_deviasi


def hitung_standar_deviasi(data):
    rata_rata_data = hitung_rata_rata(data)
    varians = 0
    for item in data:
        varians += (item - rata_rata_data) ** 2
    varians /= len(data)
    standar_deviasi = varians ** (1/2)
    return standar_deviasi

# Definisikan fungsi untuk menghitung rata-rata dan standar deviasi
# setiap kolom pada tabel_properti yang diberikan oleh key dict.


def deskripsi_properti(tabel):
    for key in tabel.keys():
        print('Rata-rata ' + key + ':')
        print(hitung_rata_rata(tabel[key]))
        print('Standar deviasi ' + key + ':')
        print(hitung_standar_deviasi(tabel[key]))
        print('')


# Panggil fungsi deskripsi_properti untuk menghitung rata-rata
# dan standar deviasi setiap kolom pada tabel_properti
deskripsi_properti(tabel_properti)

# Hitung nilai standar deviasi dari kedua data yang dimiliki
print('Standar deviasi data1:')
print(hitung_standar_deviasi(data1))
print('Standar deviasi data2:')
print(hitung_standar_deviasi(data2))
# Hitung nilai rata-rata dari kedua data yang dimiliki
print('Rata-rata data1:')
print(hitung_rata_rata(data1))
print('Rata-rata data2:')
print(hitung_rata_rata(data2))
