# saldo = 1000000
# tarik_saldo = int(input("Berapa jumlah uang yang mau anda ambil: "))
# if(saldo < tarik_saldo):
#     print("Saldo tidak mencukupi")
# else:
#     print("Saldo mencukupi")
'''
bil = int(input("Masukka Bilangan: "))
var_kondisi = bil >= 5
if var_kondisi:
    print("Bilangan lebih besar atau sama dengan 5")
else:
    print("Bilangan lebih kecil dari 5")
'''
'''
a = 7
if (a <= 3):
    a = a + 3
if (a <= 10):
    a = a + 10
if (a <= 20):
    a = a + 20
elif (a <= 40):
    a = a + 40
print(a)
'''
'''
nilai = 85
if (nilai >= 80):
    ch = 'A'
if (nilai >= 70):
    ch = 'B'
if (nilai >= 60):
    ch = 'C'
if (nilai >= 50):
    ch = 'D'
    if (nilai >= 40):
        ch = 'E'
print(ch)
'''
'''
x = 60
if x % 3 == 0:
    print("Fizz", end=" ")
if x % 5 == 0:
    print("Bazz")
'''
# def update_a(a):
#     a[0] = 3
#     a = [1,2]

# a = [0,1]
# update_a(a)
# print(a)

# i = 50
# print(type(i))
# f = float(i)
# print(type(f))

# def tambah(a,b):
#     a += 1
#     b += 1

# a = 4
# b = 5
# tambah(a,b)
# print(a,b)

# def tambah(a,b):
#     a += 100
#     b += 50
#     return(a,b)

# a=20
# b=10

# b,a = tambah(a,b)
# print(a,b)

# def haha(x):
#     a = x
#     a = [100]
#     a[0] = 100

# def hihi(x):
#     x[0] = 150

# list_a = [50]

# print(list_a)
# haha(list_a)
# print(list_a)
# hihi(list_a)
# print(list_a)

# print(chr(ord("B") + 10))

# now = 50

# def go():
#     global now
#     next = now * 100
#     now = next
#     next += 50
#     print(next)

# go()


# def cetak1(x):
#     for i in range()

# def cetak1(x):
#     for i in range(x):
#         print("x",end="")
#     print(".",end="")

# def cetak2(x):
#     for i in range(1,x+1):
#         cetak1(i)

# print(cetak2(4))

# def lalala(num1,num2):
#     ans = 0 
#     for i in range(num2):
#         ans += num1
#     return ans

# def lilili(num1,num2):
#     ans = 0
#     for i in range(num2):
#         ans += lalala(num1,num2)
#     return ans

# print(lilili(325,2))

# angka = int(input())

# for i in range(1,angka+1):
#     if angka%i== 0:
#         print(i ,True)
#     else:
#         print(i ,False)

# N =  int(input())
# K = 0
# for i in range(1,N+1):
#     B = float(input())
#     K += B

# print(K/N) 
# x = 10

# def tambah():
#     y = x + 100
#     z = y

# tambah()
# print(tambah())

# hasil = 0 
# for i in range(5,101):
#     if i / 2 == 0 and i / 8 != 0:
#         print(hasil = hasil +  1)
#     else:
#         continue

# nomer 3
# a = int(input())
# b = int(input())
# c = int(input())

# i = 1

# suku = i**b

# while i < c and suku < c:
#     print(suku)
#     suku = (1 + (i * a))**b
#     i = i + 1
    
# nomer 4
n = int(input())
k = int(input())

for i in range(n):
    print(-n,"/ ( ",k,"-",i,") =",-n / (k-n))
