n = int(input())
cek = 1
for i in range(n):
   bilangan = int(input())
   jumlah = 1
   while jumlah > 0:
        if jumlah % cek == 0 and jumlah % bilangan == 0:
           cek = jumlah
           break
        jumlah += 1
print(cek)
