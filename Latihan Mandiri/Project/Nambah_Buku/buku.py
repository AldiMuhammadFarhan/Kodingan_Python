# buat list untuk menyimpan data dan keperluan
nama = []
penerbit = []
stop = False
i = 0
# perulangan nambah buku
while(not stop):
    nama_buku = input("Inputkan nama buku yang ke-{}: ".format(i))
    nama.append(nama_buku)
    penerbit_buku = input("Inputkan penerbit buku yang ke-{}: ".format(i))
    penerbit.append(penerbit_buku)

    # Increment i
    i += 1
    
    tanya = input("Mau isi lagi? (y/t): ")
    if(tanya == "t"): 
        stop = True

# cetak output
print("=" * 30)
print("ada",len(nama),"nama buku")
for n in nama:
    print("-",n)
print("\n")
print("ada",len(penerbit),"penerbit buku")
for p in penerbit:
    print("-",p)

    
