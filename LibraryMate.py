# Import library math
import math
# Fungsi math.ceil()
# Menerima input berupa bilangan dan mengembalikan pembulatan ke atas untuk bilangan input.
print(">>> Fungsi math.ceil()")
x = 10.32
y = 13.87
x_ceil = math.ceil(x)
y_ceil = math.ceil(y)
print(x_ceil)
print(y_ceil)
# Fungsi math.floor()
# Menerima input berupa bilangan dan mengembalikan hasil pembulatan ke bawah untuk bilangan input.
print(">>> Fungsi math.floor()")
x_floor = math.floor(x)
y_floor = math.floor(y)
print(x_floor)
print(y_floor)
# Fungsi math.fabs()
# Menerima input berupa bilangan dan mengembalikan hasil absolut dari bilangan input.
print(">>> Fungsi math.fabs()")
x = 10.32
y = -13.87
x = math.fabs(x)
y = math.fabs(y)
print(x)
print(y)
# Fungsi math.factorial()
# Menerima input berupa bilangan dan mengembalikan hasil faktorial dari bilangan input
print(">>> Fungsi math.factorial()")
x_factorial = math.factorial(5)
print(x_factorial)
# Fungsi math.fsum()
# Menerima input berupa tipe data collection (tuple, list, etc.) dan mengembalikan hasil 
# penjumlahan setiap elemennya.
print(">>> Fungsi math.fsum()")
x = [1, 2, 3, 4, 5, 6, -6, -5, -4]
total = math.fsum(x)
print(total)
# Fungsi math.log()
'''
Menerima input berupa dua buah bilangan (asumsikan x dan y) dan mengembalikan sebuah bilangan (z) di 
mana z merupakan hasil log basis y dari x (atau dengan kata lain x merupakan hasil pemangkatan dari z terhadap y)
'''
print(">>> Fungsi math.log()")
# x = log basis 2 dari 8
x = math.log(8,2)
# y = log basis 3 dari 81
y = math.log(81,3)
# z = log basis 10 dari 10000
z = math.log(10000,10)
print(x)
print(y)
print(z)
# Fungsi math.sqrt()
# Menerima input berupa sebuah bilangan dan mengembalikan hasil akar pangkat dua (akar kuadrat) dari bilangan tsb
print(">>> Fungsi math.sqrt()")
# akar kuadrat dari 100
x = math.sqrt(100)
print(x)
# akar kuadrat dari 2
y = math.sqrt(2)
print(y)
# Fungsi math.copysign()
'''
Menerima input berupa dua buah 
bilangan dan mengembalikan tanda bilangan pertama yang dikalikan dengan tanda positif/ negatif dari bilangan kedua
'''
print(">>> Fungsi math.copysign()")
x = 10.32
y = -13.87
z = -15
x = math.copysign(x,z)
y = math.copysign(y,z)
z = math.copysign(z,10)
print(x)
print(y)
print(z)