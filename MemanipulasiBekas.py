'''
Fungsi open() menerima 2 parameter, di mana parameter pertama merupakan nama dari file yang 
ingin dibuka/ dibuat dan mode yang berkaitan dengan aksi yang ingin dilakukan terhadap file yang telah terbuka.
Sebagai contoh: 
file = open("hello.txt", "r")
argumen/ parameter "r" mengartikan bahwa file yang akan dibuka berada dalam mode “read” sehingga nantinya aku 
tidak dapat menambahkan/ menuliskan ulang isi tulisan dari file “hello.txt”.Perintah ini dapat digunakan untuk 
menutup file yang telah aku buka.
file.close()
w: write, mode ini dapat aku gunakan untuk menulis ke dalam sebuah berkas teks, jika berkas tidak tersedia, 
maka Python akan secara otomatis membuat sebuah berkas baru dengan nama yang telah di spesifikasikan. 
Saat menulis dengan menggunakan mode ini, jika file semula tidak kosong, maka isi yang sebelumnya terdapat di 
dalam berkas akan terhapus.
a: append, mode ini dapat aku gunakan untuk menambahkan isi dari sebuah berkas teks. Mode ini juga akan membuat
sebuah berkas teks baru dengan nama yang telah kita spesifikasikan jika berkas teks tidak tersedia.
w+: write+, mode ini dapat aku gunakan untuk membaca ataupun menuliskan isi dari sebuah berkas teks.
a+: append+, mode ini dapat aku gunakan untuk  membaca ataupun menambahkan isi dari sebuah berkas teks.
'''

# Semisal
# Membaca file hello.txt dengan fungsi read()
print(">>> Membaca file hello.txt dengan fungsi read()")
file = open("hello.txt", "r")
content = file.read()
file.close()
print(content)
# Membaca file hello.txt dengan fungsi readline()
print(">>> Membaca file hello.txt dengan fungsi readline()")
file = open("hello.txt", "r")
first_line = file.readline()  # untuk membaca per baris
second_line = file.readline()
file.close()
print(first_line)
print(second_line)

'''
Fungsi readlines() akan mengembalikan sebuah list yang setiap elemennya 
merupakan setiap baris dalam sebuah berkas teks.
'''
# Membaca file hello.txt dengan fungsi readlines()
print(">>> Membaca file hello.txt dengan fungsi readlines()")
file = open("hello.txt", "r")
all_lines = file.readlines()
file.close()
print(all_lines)
# Membaca file hello.txt dengan menerapkan looping
print(">>> Membaca file hello.txt dengan menerapkan looping")
file = open("hello.txt", "r")
for line in file:
    print(line)
file.close()

# Menulis ke file hello.txt
file = open("hello.txt", "w")
file.write("Sekarang kita belajar menulis dengan menggunakan Python")
file.write("Menulis konten file dengan mode w (write).")
file.close()

# Menulis ke file dengan mode append
file = open("hello.txt", "a")
file.writelines([
    "Sekarang kita belajar menulis dengan menggunakan Python",
    "Menulis konten file dengan mode a (append)."
])
file.close()
