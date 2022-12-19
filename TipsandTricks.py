# Tuple
print(">>> Tuple")
tuple_menu = ('Gado-gado','Ayam Goreng','Rendang','Ketoprak')
jumlah_menu = len(tuple_menu)
print(jumlah_menu)
# List
print(">>> List")
list_menu = ['Gado-gado','Ayam Goreng','Rendang','Ketoprak']
jumlah_menu = len(list_menu)
print(jumlah_menu)
# Konversi tipe data
print(">>> Konversi tipe data")
list_buah = ['Apel', 'Apel', 'Jeruk', 'Markisa', 'Jeruk', 'Markisa', 'Apel']
# mengkonversi sebuah list ke sebuah set
set_buah = set(list_buah)
print(set_buah)
# mengkonversi sebuah set ke sebuah list
list_buah = list(set_buah)
list_buah.sort()
print(list_buah)