import pandas as pd
import datetime
import matplotlib.pyplot as plt

dataset = pd.read_csv(
    'https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(
    lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['gmv'] = dataset['item_price']*dataset['quantity']

plt.figure(figsize=(15, 5))
'''
color: mengubah warnanya (sama seperti di title)
linewidth: mengubah ketebalan line/garisnya (dalam satuan px)
linestyle: mengubah jenis dari garis. Misalnya '-' atau 'solid' untuk garis tak terputus 
            (seperti pada default), '--' atau 'dashed' untuk garis putus-putus, ':' atau 'dotted' untuk garis 
            berupa titik-titik, bisa juga '-.' atau ‘dashdot’ untuk garis dan titik bergantian.
marker: mengubah tipe points/titik data di chart. Ada banyak sekali kemungkinan nilai untuk marker ini, yang 
            biasanya digunakan yaitu ‘.’ untuk bulatan kecil/titik, ‘o’ untuk bulatan agak besar, ‘s’ untuk 
            persegi, ‘D’ untuk diamond/wajik, dan bentuk-bentuk lain seperti ‘+’, ‘x’, ‘|’, ‘*’.
'''
dataset.groupby(['order_month'])['gmv'].sum().plot(
    color='green', marker='o', linestyle='-.', linewidth=2)
'''
loc: digunakan untuk menentukan posisi title, misalnya ‘left’ untuk membuat rata kiri, ‘right’ untuk rata kanan, 
        dan ‘center’ untuk meletakkannya di tengah. Jika tidak didefinisikan, maka defaultnya title ada di tengah.
pad: digunakan untuk menambahkan jarak antara judul ke grafik (dalam satuan px), misalnya kita tidak ingin judulnya 
        terlalu menempel dengan grafiknya, jadi kita beri jarak.
fontsize: digunakan untuk mengganti ukuran font/huruf (dalam satuan px).
color: digunakan untuk mengganti warna huruf judul. Kita bisa menggunakan warna dasar dengan kata seperti ‘blue’, 
        ‘red’, ‘orange’, dsb. Bisa juga dengan hex string, misalnya '#42DDF5' untuk warna biru muda.

'''
plt.title('Monthly GMV Year 2019', loc='center',
          pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount (in Billions)', fontsize=15)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
# diset agar sumbu-y nya dimulai dari 0,
# Untuk mengatur batas maksium, kita tambahkan juga parameter ymax
# Kita juga bisa mengatur batas minimum dan maksimum sumbu-x dengan function plt.xlim.
plt.ylim(ymin=0)
'''
Nilai-nilai di sumbu x dan y bisa diakses melalui function plt.xticks() dan plt.yticks().

mengubah ticks di sumbu-y menjadi milyar,digantikan dengan nilai baru yaitu nilai awal dibagi 
dengan 1 milyar (1000000000).
'''
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))
'''
Perhatikan bahwa ada beberapa parameter yang diset saat menggunakan plt.text. Dua angka pertama itu adalah 
    koordinat, x dan y. Saat set transform=fig.transFigure, maka koordinatnya berkisar 0 sampai 1 (untuk x dari 
    kanan ke kiri, dan untuk y, dari bawah ke atas).

Jika parameter transform tidak diisi, maka koordinatnya dalam satuan inch (Dalam contoh ini, dari 0-15 dari kiri ke
    kanan, dan 0-5 dari bawah ke atas). Seperti halnya title atau label, dimungkinkan juga untuk set warna dan 
    ukuran hurufnya.
'''
plt.text(0.45, 0.72, 'The GMV increased significantly on October 2019',
         transform=fig.transFigure, color='red')
# Untuk menyimpan / save gambar
'''
Untuk mengetahui format lengkapnya, kita bisa menggunakan code berikut:
    plt.gcf().canvas.get_supported_filetypes()

Ada berbagai parameter yang bisa diatur saat menyimpan gambar, antara lain:
dpi: Resolusi gambar (dots per inch). 
quality: Kualitas gambar (hanya berlaku jika formatnya jpg atau jpeg), bisa diisi nilai 1 
            (paling buruk) hingga 95 (paling bagus).
facecolor: Memberikan warna bagian depan figure, di luar area plot 
edgecolor: Memberikan warna pinggiran gambar
transparent: Jika nilainya True, maka gambarnya jadi transparan (jika filenya png)
 
Tapi biasanya, parameter-parameter ini tidak digunakan karena grafik di file gambar bisa jadi 
berbeda dengan yang muncul saat menjalankan code di python.
'''
plt.savefig('monthly_gmv.png', quality=95)
plt.show()
