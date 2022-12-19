import re
rupiah = 'Kemarin (sabtu) saya mendapat beasiswa (Rp 10.000.000), \
kemudian mendapat doorpize sebesar (Rp 1.000.000).'
uang = rupiah.replace('.', '')
uang2 = re.findall("\d+",uang)
uang3 = [int(i) for i in uang2]
hasil = sum (uang3)
print("Rp ", hasil)