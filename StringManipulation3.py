# Fitur .strip()
# Menghilangkan kelebihan spasi pada awal dan akhir string.
print(">>> Fitur .strip()")
kata_sambutan = ' halo, selamat siang! '
kata_sambutan = kata_sambutan.strip()
print(kata_sambutan)
# Fitur .lstrip()
# Menghilangkan kelebihan spasi pada awal string.
print(">>> Fitur .lstrip()")
kata_sambutan = ' halo, selamat siang! '
kata_sambutan = kata_sambutan.lstrip()
print(kata_sambutan)
# Fitur .rstrip()
# Menghilangkan kelebihan spasi pada akhir string.
print(">>> Fitur .rstrip()")
kata_sambutan = ' halo, selamat siang! '
kata_sambutan = kata_sambutan.rstrip()
print(kata_sambutan)
# Fitur .capitalize()
# Mengubah elemen pertama dari string menjadi huruf kapital.
print(">>> Fitur .capitalize()")
judul_buku = 'belajar bahasa Python'
print(judul_buku.capitalize())
# Fitur .lower()
# Mengubah seluruh huruf dalam teks (string) menjadi huruf kecil
print(">>> Fitur .lower()")
judul_buku = 'Belajar Bahasa PYTHON.'
print(judul_buku.lower())
# Fitur .upper()
# Mengubah seluruh huruf dalam teks (string) menjadi huruf besar
print(">>> Fitur .upper()")
judul_buku = 'Belajar Bahasa PYTHON.'
print(judul_buku.upper())
# Fitur .split()
# Memecah sebuah string berdasarkan string lainnya ke dalam sebuah list.
print(">>> Fitur .split()")
bilangan = "ani dan budi dan wati dan johan"
karakter = bilangan.split("dan")
print(karakter)
kata = bilangan.split(" ")
print(kata)
# Fitur .join()
# Menggabungkan sebuah list yang berisikan string berdasarkan sebuah string yang telah didefinisikan.
print(">>> Fitur .join()")
pemisah = " dan "
karakter = ["Ricky", "Peter", "Jordan"]
kalimat = pemisah.join(karakter)
print(kalimat)
# Fitur .replace()
# Menggantikan kemunculan suatu string tertentu dengan string lainnya dalam sebuah string.
print(">>> Fitur .replace()")
kalimat = "apel malang apel yang paling segar, apel sehat, apel nikmat"
kalimat = kalimat.replace("apel", "jeruk")
print(kalimat)
teks = "Apel malang adalah apel termanis dibanding apel-apel lainnya"
# Fitur .find()
# Mengembalikan posisi dari sebuah teks (sub-string) lainnya dalam sebuah string.
print(">>> Fitur .find()")
print(teks.find("Apel"))
print(teks.find("malang"))
# Fitur .count()
# Menghitung jumlah kemunculan sebuah teks (string) lainnya dalam suatu string (string yang dicari bersifat case sensitive).
print(">>> Fitur .count()")
kemunculan_kata_apel = teks.count("apel")
print(kemunculan_kata_apel)
# Fitur .startswith()
# Mengembalikan nilai kebenaran True ketika sebuah teks (string) diawali dengan sebuah teks lainnya.
print(">>> Fitur .startswith()")
teks = "Apel malang adalah apel termanis dibanding apel-apel lainnya"
print(teks.startswith("Apel"))
print(teks.startswith("apel"))
# Fitur .endswith()
# Mengembalikan nilai kebenaran True ketika sebuah teks (string) diakhiri dengan sebuah teks lainnya.
print(">>> Fitur .endswith()")
print(teks.endswith("lainnya"))
print(teks.endswith("apel"))
