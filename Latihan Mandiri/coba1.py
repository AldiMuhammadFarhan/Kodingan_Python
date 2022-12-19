# a,b = input().split(" ")
# x,y = int(a),int(b)
# for i in range(y):
#     w,e,r = input().split(" ")
#     p,o,i = int(w),int(e),int(r)
#     if p < 0 and o < 0 and i < 0:
#         print("Terdeteksi sirkuit jalan rusak")
#         break
#     else:
#         continue

# s1 = "aldi"
# s2 = "aldi"
# print(s1+s2)
# print(s1-s2)

# s1 = 'Tidak Mungkin Aku Suka Ngoding'
# s2 = s1[-7:]
# print(s2)

# s = '5G sudah ada di depan mata!'
# print(s.capitalize())

# s = '5G sudah ada di depan mata!'
# print(s.title())

# s1 = 'Hallo'
# s2 = 'Dunia'
# print(len(2 * (s1 + s2)))

# s1 = 'Telyu'
# s2 = 'telyu'
# print (s1[:2] == s2[:2])

# s = 'Telkom University Membuka Pendaftaran!'
# print(s.sentence())

# text = 'seratus dua puluh ribu rupiah (Rp 125.000), dan lima puluh rupiah (Rp 50)'
# newtext = text.replace(' ', '\n')
# print(newtext)
# newtext = newtext.replace(')', ']')
# print(newtext)
# def x(n):
#     hasil = 2*n
#     if hasil == 0:
#         return hasil + 1
#     return hasil 
# print(x(0))
# print(x(1))
# print(x(2))
# def a(n):
#    if n == 0: return 0
#    if n == 1: return 4
#    else:  return 6*a(n-1)-5*a(n-2)
# print(a(4))
# def x(n):
#     # fix the following code
#     if n == 0: return 1
#     elif n == 1: return 2*x(0)
#     elif n == 2: return 2*x(1)
#     else: return 2*x(n-1)%101
# print(x(3))
# def x(n):
#     return (n-1)+1
# print(x(9998))
# def x(n):
#     # fix the following code
#     if n == 0: return 0
#     elif n == 1: return x(0)+1
#     elif n == 2: return x(1)+2
#     elif n == 3: return x(2)+3
#     else: return x(n-1) + n
# print(x(4))
# def a(n):
#    if n == 0: return 0
#    if n == 1: return 4
#    else:  return 6*a(n-1)-5*a(n-2)
# print(a(20))

# tabungan_pertama = int(input())
# n = int(input())
# jumlah = 0
# for i in range(1,n+1):
#     jumlah = tabungan_pertama*n + 1000
# print(jumlah)

# n = int(input())
# m = int(input())
# i = n
# while m >= i:
#     print(i,end=" ")
#     i = i+1

# jumlah = 0
# bilangan = 1
# for i in range(bilangan,bilangan+1000):
#     jumlah += i
# print(jumlah)

# jam = int(input())
# jumlah_jam = 0
# jumlah_hari = 0
# while jam > 0:
#     jumlah_jam += jam
#     jumlah_hari += 1
#     jam = int(input())

# print(jumlah_jam/jumlah_hari)
    
# def x(n):
#     hasil = 0
#     for i in range(n+1):
#         hasil =  x(i-1)+i
#     return hasil

# print(x(3))

# n = int(input())
# jumlah = 0
# i = 0
# while i <= n:
#     jumlah = jumlah + 1/2**i
#     i = i + 1

# print('{:.5f}'.format(jumlah))

# fungsi logika matematika 1
# def x(n):
#     jumlah = 0
#     for i in range(n+1):
#         jumlah = 2**i
#     return jumlah
# print(x(1))

# fungsi logika matematika 2
# def x(n):
#     jumlah = 0
#     for i in range(n+1):
#         jumlah = 2*(i-1)
#     return jumlah
# print(x(10000000))
# print(19999998%100)

# fungsi logika matematika 2
# def x(n):
#     jumlah = 0
#     for i in range(n+1):
#         jumlah = x(i-1) + i
#     return jumlah
# print(x(20))

# def what(n):
#     return ((n+1)*(3*n+2))//2
# print(what(100))

# awal = 8
# akhir = 7015
# jumlah = 0
# while awal <= akhir:
#         jumlah += awal
#         awal += 7
# for i in range(awal,akhir+1):
#     if i % 6 == 0:
#         jumlah+=1
# print(jumlah)
# jumlah = 0
# for i in range(0,101):
#     if i%5 != 0 and i%7 != 0:
#         jumlah+=1
# print(jumlah) 

print("habib")